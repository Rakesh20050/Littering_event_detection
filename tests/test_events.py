
import unittest

from src.event.event_state_machine import (
    EventObservation,
    EventState,
    EventStateMachine,
)



def observation(
    timestamp,
    *,
    holding=False,
    release=False,
    landed=False,
    left=False,
    bin_entry=False,
    pickup=False,
    worker=False,
    occluded=False,
    incomplete=False,
    confidence=0.9,
    person_id=21,
    waste_id=8,
):
    return EventObservation(
        timestamp=timestamp,
        person_track_id=person_id,
        waste_track_id=waste_id,
        holding_observed=holding,
        release_observed=release,
        waste_landed_observed=landed,
        person_left_observed=left,
        entered_bin_observed=bin_entry,
        pickup_observed=pickup,
        worker_activity=worker,
        occlusion_or_crowd=occluded,
        evidence_incomplete=incomplete,
        observation_confidence=confidence,
    )


class TestEventStateMachine(unittest.TestCase):
    def setUp(self):
        self.machine = EventStateMachine(min_event_confidence=0.65)

    def test_complete_littering_candidate(self):
        samples = [
            observation("2026-10-10T10:00:00Z", holding=True),
            observation("2026-10-10T10:00:01Z", release=True),
            observation("2026-10-10T10:00:02Z", landed=True),
            observation("2026-10-10T10:00:05Z", left=True),
        ]

        result = None
        for sample in samples:
            result = self.machine.update(sample) or result

        self.assertIsNotNone(result)
        self.assertEqual(
            result.event_type,
            EventState.LITTERING_CANDIDATE.value,
        )
        self.assertEqual(result.person_track_id, 21)
        self.assertEqual(result.waste_track_id, 8)
        self.assertIn("waste released", result.evidence_timeline)
        self.assertIn("waste landed", result.evidence_timeline)
        self.assertIn("person left", result.evidence_timeline)
        self.assertTrue(result.review_required)

    def test_proper_disposal(self):
        self.machine.update(
            observation("2026-10-10T10:00:00Z", holding=True)
        )
        result = self.machine.update(
            observation("2026-10-10T10:00:01Z", bin_entry=True)
        )

        self.assertEqual(
            result.event_type,
            EventState.PROPER_DISPOSAL.value,
        )

    def test_pickup(self):
        self.machine.update(
            observation("2026-10-10T10:00:00Z", holding=True)
        )
        self.machine.update(
            observation("2026-10-10T10:00:01Z", release=True)
        )
        result = self.machine.update(
            observation("2026-10-10T10:00:02Z", pickup=True)
        )

        self.assertEqual(result.event_type, EventState.PICKUP.value)

    def test_existing_ground_waste_does_not_trigger_event(self):
        result = self.machine.update(
            observation("2026-10-10T10:00:00Z")
        )

        self.assertIsNone(result)
        self.assertEqual(self.machine.state, EventState.NO_EVENT)

    def test_worker_activity_requires_review(self):
        self.machine.update(
            observation("2026-10-10T10:00:00Z", holding=True)
        )
        result = self.machine.update(
            observation("2026-10-10T10:00:01Z", worker=True)
        )

        self.assertEqual(result.event_type, EventState.UNCERTAIN.value)
        self.assertTrue(result.review_required)

    def test_occlusion_requires_review(self):
        self.machine.update(
            observation("2026-10-10T10:00:00Z", holding=True)
        )
        result = self.machine.update(
            observation("2026-10-10T10:00:01Z", occluded=True)
        )

        self.assertEqual(result.event_type, EventState.UNCERTAIN.value)
        self.assertTrue(result.review_required)

    def test_low_confidence_requires_review(self):
        self.machine = EventStateMachine(min_event_confidence=0.95)

        samples = [
            observation("2026-10-10T10:00:00Z", holding=True),
            observation("2026-10-10T10:00:01Z", release=True),
            observation("2026-10-10T10:00:02Z", landed=True),
            observation("2026-10-10T10:00:03Z", left=True),
        ]

        result = None
        for sample in samples:
            result = self.machine.update(sample) or result

        self.assertEqual(result.event_type, EventState.UNCERTAIN.value)
        self.assertTrue(result.review_required)

    def test_accidental_drop_then_pickup(self):
        machine = EventStateMachine()

        machine.update(observation(
            "2026-10-10T10:00:00Z",
            holding=True,
        ))

        machine.update(observation(
            "2026-10-10T10:00:01Z",
            release=True,
        ))

        result = machine.update(observation(
            "2026-10-10T10:00:02Z",
            pickup=True,
        ))

        self.assertIsNotNone(result)
        self.assertEqual(result.event_type, EventState.PICKUP)
        self.assertNotEqual(
            result.event_type,
            EventState.LITTERING_CANDIDATE,
        )
    
    def test_carrying_waste_without_dropping(self):
        machine = EventStateMachine()

        result = machine.update(observation(
            "2026-10-10T10:00:00Z",
            holding=True,
        ))

        result = machine.update(observation(
            "2026-10-10T10:00:01Z",
            holding=True,
        ))

        self.assertIsNone(result)
        self.assertEqual(machine.state, EventState.HOLDING_WASTE)

    def test_incomplete_evidence_requires_review(self):
        self.machine.update(observation(
            "2026-10-10T10:00:00Z",
            holding=True,
        ))

        result = self.machine.update(observation(
            "2026-10-10T10:00:01Z",
            incomplete=True,
        ))

        self.assertIsNotNone(result)
        self.assertEqual(result.event_type, EventState.UNCERTAIN.value)
        self.assertTrue(result.review_required)

    def test_track_id_change_requires_review(self):
        self.machine.update(observation(
            "2026-10-10T10:00:00Z",
            holding=True,
        ))

        result = self.machine.update(observation(
            "2026-10-10T10:00:01Z",
            release=True,
            person_id=99,
        ))

        self.assertIsNotNone(result)
        self.assertEqual(result.event_type, EventState.UNCERTAIN.value)
        self.assertTrue(result.review_required)
        self.assertEqual(result.person_track_id, 21)

    def test_missing_track_id_during_event_requires_review(self):
        self.machine.update(observation(
            "2026-10-10T10:00:00Z",
            holding=True,
        ))

        result = self.machine.update(observation(
            "2026-10-10T10:00:01Z",
            person_id=None,
        ))

        self.assertIsNotNone(result)
        self.assertEqual(result.event_type, EventState.UNCERTAIN.value)
        self.assertTrue(result.review_required)

    def test_out_of_order_timestamp_is_rejected(self):
        self.machine.update(observation(
            "2026-10-10T10:00:02Z",
            holding=True,
        ))

        with self.assertRaises(ValueError):
            self.machine.update(observation(
                "2026-10-10T10:00:01Z",
                release=True,
            ))


if __name__ == "__main__":
    unittest.main()
