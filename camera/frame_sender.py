"""
CleanWatch AI - Frame Sender

Sends camera frames from the camera device
to the CleanWatch AI server.
"""

import cv2
import requests


class FrameSender:

    def __init__(
        self,
        server_url="http://127.0.0.1:8000",
        camera_id="CAMERA_01"
    ):

        self.server_url = server_url.rstrip("/")
        self.camera_id = camera_id

        self.frame_endpoint = (
            f"{self.server_url}/camera/frame"
        )

        self.connected = False

    def connect(self):

        try:

            response = requests.get(
                self.server_url,
                timeout=3
            )

            response.raise_for_status()

            self.connected = True

            print("AI server connected.")
            print(f"Server: {self.server_url}")

            return True

        except requests.RequestException as error:

            print("Could not connect to AI server.")
            print(error)

            self.connected = False

            return False

    def send_frame(self, frame):

        if not self.connected:

            if not self.connect():
                return False

        success, encoded = cv2.imencode(
            ".jpg",
            frame,
            [
                cv2.IMWRITE_JPEG_QUALITY,
                80
            ]
        )

        if not success:
            return False

        try:

            response = requests.post(
                self.frame_endpoint,

                files={
                    "frame": (
                        "frame.jpg",
                        encoded.tobytes(),
                        "image/jpeg"
                    )
                },

                data={
                    "camera_id": self.camera_id
                },

                timeout=3
            )

            if response.status_code == 200:
                return True

            print(
                "Frame transmission failed:",
                response.status_code
            )

            return False

        except requests.RequestException as error:

            print(
                "Connection to AI server lost:",
                error
            )

            self.connected = False

            return False

    def disconnect(self):

        self.connected = False

        print("Frame sender disconnected.")