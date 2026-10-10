"""
CleanWatch AI - Frame Sender

Sends camera frames from the camera device
to the CleanWatch AI server.

Designed for low-latency streaming:
- Sends frames continuously
- Uses a background sender thread
- Drops old frames when the network is busy
- Keeps the newest frame available
"""

from urllib import response

from urllib import response

import cv2
import requests
import threading
import time


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

        # ---------------------------------------------------
        # Latest-frame buffer
        # ---------------------------------------------------

        self.latest_frame = None
        self.frame_lock = threading.Lock()

        # Sender control
        self.running = False
        self.sender_thread = None

        # Statistics
        self.frames_sent = 0
        self.frames_dropped = 0
        self.last_send_time = 0

    # -------------------------------------------------------
    # SERVER CONNECTION
    # -------------------------------------------------------

    def connect(self):

        try:

            response = requests.get(
                self.server_url,
                timeout=2
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

    # -------------------------------------------------------
    # START BACKGROUND SENDER
    # -------------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.sender_thread = threading.Thread(
            target=self._send_loop,
            daemon=True
        )

        self.sender_thread.start()

        print("Frame sender started.")

    # -------------------------------------------------------
    # FRAME INPUT
    # -------------------------------------------------------

    def send_frame(self, frame):

        """
        Store only the newest frame.

        The background sender thread handles
        network transmission.
        """

        with self.frame_lock:

            if self.latest_frame is not None:
                self.frames_dropped += 1

            self.latest_frame = frame

        return True

    # -------------------------------------------------------
    # BACKGROUND NETWORK LOOP
    # -------------------------------------------------------

    def _send_loop(self):

        while self.running:

            frame = None

            # Get newest frame
            with self.frame_lock:

                if self.latest_frame is not None:

                    frame = self.latest_frame
                    self.latest_frame = None

            if frame is None:

                time.sleep(0.005)
                continue

            # ------------------------------------------------
            # Make sure server is connected
            # ------------------------------------------------

            if not self.connected:

                if not self.connect():

                    time.sleep(0.5)
                    continue

            # ------------------------------------------------
            # Encode frame
            # ------------------------------------------------

            success, encoded = cv2.imencode(
                ".jpg",
                frame,
                [
                    cv2.IMWRITE_JPEG_QUALITY,
                    70
                ]
            )

            if not success:
                continue

            # ------------------------------------------------
            # Send frame
            # ------------------------------------------------

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

                    timeout=1
                )
                print("Upload status:", response.status_code)
                print("Upload response:", response.text)

                if response.status_code == 200:

                    self.frames_sent += 1
                    self.last_send_time = time.time()

                else:

                    print(
                        "Frame transmission failed:",
                        response.status_code
                    )

            except requests.RequestException as error:

                print(
                    "Connection to AI server lost:",
                    error
                )

                self.connected = False

    # -------------------------------------------------------
    # STATUS
    # -------------------------------------------------------

    def get_stats(self):

        return {
            "connected": self.connected,
            "frames_sent": self.frames_sent,
            "frames_dropped": self.frames_dropped,
            "last_send_time": self.last_send_time
        }

    # -------------------------------------------------------
    # DISCONNECT
    # -------------------------------------------------------

    def disconnect(self):

        self.running = False

        if self.sender_thread is not None:

            self.sender_thread.join(
                timeout=1
            )

            self.sender_thread = None

        self.connected = False

        with self.frame_lock:
            self.latest_frame = None

        print("Frame sender disconnected.")