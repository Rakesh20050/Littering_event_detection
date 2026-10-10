
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional


class EventState(str, Enum):
    NO_EVENT = "NO_EVENT"
    HOLDING_WASTE = "HOLDING_WASTE"
    RELEASE_CANDIDATE = "RELEASE_CANDIDATE"
    WASTE_LANDED = "WASTE_LANDED"
    PERSON_LEFT = "PERSON_LEFT"
    LITTERING_CANDIDATE = "LITTERING_CANDIDATE"
    PROPER_DISPOSAL = "PROPER_DISPOSAL"
    PICKUP = "PICKUP"
    NO_LITTERING = "NO_LITTERING"
    UNCERTAIN = "UNCERTAIN"


@dataclass
class EventObservation:
    """Evidence about one person-waste interaction at a point in time.

    These signals should come from video analysis or annotated test data.
    Do not infer holding/release from proximity alone.
    """

    timestamp: str
    person_track_id: Optional[int]
    waste_track_id: Optional[int]

    holding_observed: bool = False
    release_observed: bool = False
    waste_landed_observed: bool = False
    person_left_observed: bool = False
    entered_bin_observed: bool = False
    pickup_observed: bool = False

    worker_activity: bool = False
    occlusion_or_crowd: bool = False
    evidence_incomplete: bool = False

    # Confidence in the observation signals, not identity confidence.
    observation_confidence: float = 0.0


@dataclass
class EventRecord:
    person_track_id: Optional[int]
    waste_track_id: Optional[int]
    event_type: str
    start_timestamp: str
    end_timestamp: str
    event_confidence: float
    evidence_timeline: list[str] = field(default_factory=list)
    review_required: bool = False
    state: str = EventState.NO_EVENT.value


class EventStateMachine:
    """Conservative temporal state machine for littering-event candidates."""

    def __init__(self, min_event_confidence: float = 0.65):
        if not 0.0 <= min_event_confidence <= 1.0:
            raise ValueError("min_event_confidence must be between 0 and 1")

        self.min_event_confidence = min_event_confidence
        self.reset()

    def reset(self) -> None:
        self.state = EventState.NO_EVENT
        self.person_track_id = None
        self.waste_track_id = None
        self.start_timestamp = None
        self.last_timestamp = None
        self.evidence_timeline = []
        self.confidences = []
        self.review_required = False

    def _finish(
        self,
        event_type: EventState,
        timestamp: str,
        confidence: Optional[float] = None,
        review_required: bool = False,
    ) -> EventRecord:
        scores = self.confidences or [0.0]
        final_confidence = (
            sum(scores) / len(scores) if confidence is None else confidence
        )

        record = EventRecord(
            person_track_id=self.person_track_id,
            waste_track_id=self.waste_track_id,
            event_type=event_type.value,
            start_timestamp=self.start_timestamp or timestamp,
            end_timestamp=timestamp,
            event_confidence=round(max(0.0, min(1.0, final_confidence)), 3),
            evidence_timeline=list(self.evidence_timeline),
            review_required=review_required,
            state=event_type.value,
        )
        self.reset()
        return record

    def update(self, obs: EventObservation) -> Optional[EventRecord]:
        """Consume one chronological observation.

        Returns an EventRecord when an outcome is reached; otherwise None.
        The caller should maintain separate machines for separate
        person-waste interaction candidates.
        """
        if not 0.0 <= obs.observation_confidence <= 1.0:
            raise ValueError("observation_confidence must be between 0 and 1")

        if self.last_timestamp is not None and obs.timestamp < self.last_timestamp:
            raise ValueError("Observations must be chronological")

        self.last_timestamp = obs.timestamp

        # An event must be associated with actual tracked objects.
        if obs.person_track_id is None or obs.waste_track_id is None:
            if self.state not in (EventState.NO_EVENT, EventState.UNCERTAIN):
                self.review_required = True
                return self._finish(
                    EventState.UNCERTAIN,
                    obs.timestamp,
                    review_required=True,
                )
            return None

        # Do not silently combine observations from different tracks.
        if self.state != EventState.NO_EVENT and (
            obs.person_track_id != self.person_track_id
            or obs.waste_track_id != self.waste_track_id
        ):
            return self._finish(
                EventState.UNCERTAIN,
                obs.timestamp,
                review_required=True,
            )

        if self.state == EventState.NO_EVENT:
            if not obs.holding_observed:
                # Existing ground waste or mere proximity is not an event.
                return None

            self.person_track_id = obs.person_track_id
            self.waste_track_id = obs.waste_track_id
            self.start_timestamp = obs.timestamp
            self.state = EventState.HOLDING_WASTE
            self.evidence_timeline.append("waste held")
            self.confidences.append(obs.observation_confidence)
            return None

        self.confidences.append(obs.observation_confidence)

        if obs.worker_activity:
            self.evidence_timeline.append("worker activity observed")
            return self._finish(
                EventState.UNCERTAIN,
                obs.timestamp,
                review_required=True,
            )

        if obs.occlusion_or_crowd or obs.evidence_incomplete:
            self.evidence_timeline.append("evidence incomplete or occluded")
            return self._finish(
                EventState.UNCERTAIN,
                obs.timestamp,
                review_required=True,
            )

        if obs.entered_bin_observed:
            self.evidence_timeline.append("waste entered bin")
            return self._finish(
                EventState.PROPER_DISPOSAL, obs.timestamp
            )

        if obs.pickup_observed:
            self.evidence_timeline.append("waste picked up")
            return self._finish(
                EventState.PICKUP, obs.timestamp
            )

        if (
            self.state == EventState.HOLDING_WASTE
            and obs.release_observed
        ):
            self.state = EventState.RELEASE_CANDIDATE
            self.evidence_timeline.append("waste released")
            return None

        if (
            self.state == EventState.RELEASE_CANDIDATE
            and obs.waste_landed_observed
        ):
            self.state = EventState.WASTE_LANDED
            self.evidence_timeline.append("waste landed")
            return None

        if (
            self.state == EventState.WASTE_LANDED
            and obs.person_left_observed
        ):
            self.state = EventState.PERSON_LEFT
            self.evidence_timeline.append("person left")
            confidence = (
                sum(self.confidences) / len(self.confidences)
                if self.confidences else 0.0
            )

            # A candidate is not a final accusation. Low confidence
            # requires review rather than an automatic littering label.
            if confidence < self.min_event_confidence:
                return self._finish(
                    EventState.UNCERTAIN,
                    obs.timestamp,
                    confidence=confidence,
                    review_required=True,
                )

            self.state = EventState.LITTERING_CANDIDATE
            self.evidence_timeline.append("littering sequence supported")
            return self._finish(
                EventState.LITTERING_CANDIDATE,
                obs.timestamp,
                confidence=confidence,
                review_required=True,
            )

        return None
