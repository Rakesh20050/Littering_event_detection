"""
CleanWatch AI - Video Stream

Handles video capture from:
    1. Laptop webcam
    2. USB camera
    3. Network/mobile camera stream
"""

import cv2


class VideoStream:

    def __init__(
        self,
        source=0,
        width=1280,
        height=720
    ):
        self.source = source
        self.width = width
        self.height = height
        self.capture = None

    def start(self):
        """Open the camera/video source."""

        self.capture = cv2.VideoCapture(self.source)

        if not self.capture.isOpened():
            raise RuntimeError(
                f"Could not open camera source: {self.source}"
            )

        # Request desired resolution
        self.capture.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            self.width
        )

        self.capture.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            self.height
        )

        print("Camera connected.")
        print(f"Source: {self.source}")

        return self

    def read(self):
        """Read one frame from the camera."""

        if self.capture is None:
            raise RuntimeError(
                "Camera has not been started."
            )

        success, frame = self.capture.read()

        if not success:
            return None

        return frame

    def stop(self):
        """Release the camera."""

        if self.capture is not None:
            self.capture.release()
            self.capture = None

        print("Camera released.")