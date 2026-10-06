"""
CleanWatch AI
Camera Stream Manager

Receives frames from the camera client and makes the
latest frame available to the AI pipeline and Control Room.
"""

import threading
import time
import cv2


class CameraStreamManager:

    def __init__(self):
        self.latest_frame = None
        self.camera_id = None
        self.last_update = None
        self.lock = threading.Lock()

    def update_frame(self, frame, camera_id):
        """Store the newest camera frame."""

        with self.lock:
            self.latest_frame = frame
            self.camera_id = camera_id
            self.last_update = time.time()

    def get_frame(self):
        """Return the latest frame."""

        with self.lock:
            if self.latest_frame is None:
                return None

            return self.latest_frame.copy()

    def get_status(self):
        """Return current camera connection status."""

        with self.lock:

            if self.last_update is None:
                return {
                    "connected": False,
                    "camera_id": self.camera_id,
                    "last_update": None
                }

            seconds_since_update = time.time() - self.last_update

            return {
                "connected": seconds_since_update < 5,
                "camera_id": self.camera_id,
                "last_update": self.last_update
            }


camera_manager = CameraStreamManager()