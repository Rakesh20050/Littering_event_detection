"""
CleanWatch AI - Camera Client

Camera
   ↓
OpenCV
   ↓
Frame Sender
   ↓
AI Server
"""

import cv2

from camera.video_stream import VideoStream
from camera.frame_sender import FrameSender

from camera.camera_config import (
    CAMERA_SOURCE,
    CAMERA_ID,
    AI_SERVER_URL,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    SHOW_PREVIEW
)


def main():

    print("=" * 60)
    print("             CLEANWATCH AI")
    print("              CAMERA CLIENT")
    print("=" * 60)

    print()
    print("Camera ID:", CAMERA_ID)
    print("AI Server:", AI_SERVER_URL)
    print()

    # -------------------------------------------------------
    # Camera
    # -------------------------------------------------------

    camera = VideoStream(
        source=CAMERA_SOURCE,
        width=FRAME_WIDTH,
        height=FRAME_HEIGHT
    )

    # -------------------------------------------------------
    # Frame Sender
    # -------------------------------------------------------

    sender = FrameSender(
        server_url=AI_SERVER_URL,
        camera_id=CAMERA_ID
    )

    try:

        camera.start()

        # ---------------------------------------------------
        # Connect to AI server
        # ---------------------------------------------------

        if not sender.connect():

            print()
            print("WARNING:")
            print("AI server is not running.")
            print("Camera preview will continue,")
            print("but frames cannot be transmitted.")
            print()

        else:

            # Start background frame sender
            sender.start()

            print()
            print("Camera is running.")
            print("Press Q to stop.")
            print()

        frame_count = 0

        # ---------------------------------------------------
        # Main camera loop
        # ---------------------------------------------------

        while True:

            frame = camera.read()

            if frame is None:

                print("Camera frame unavailable.")
                break

            # ------------------------------------------------
            # SEND FRAME TO AI SERVER
            # ------------------------------------------------

            if sender.connected:

                sender.send_frame(frame)

            frame_count += 1

            # ------------------------------------------------
            # LOCAL PREVIEW
            # ------------------------------------------------

            if SHOW_PREVIEW:

                display_frame = frame.copy()

                status = (
                    "AI SERVER: CONNECTED"
                    if sender.connected
                    else "AI SERVER: DISCONNECTED"
                )

                cv2.putText(
                    display_frame,
                    status,
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0)
                    if sender.connected
                    else (0, 0, 255),
                    2
                )

                cv2.putText(
                    display_frame,
                    f"Camera: {CAMERA_ID}",
                    (20, 75),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    display_frame,
                    f"Frames: {frame_count}",
                    (20, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                )

                cv2.imshow(
                    "CleanWatch AI - Camera",
                    display_frame
                )

            # ------------------------------------------------
            # Keyboard control
            # ------------------------------------------------

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                break

    except KeyboardInterrupt:

        print("\nCamera stopped.")

    except Exception as error:

        print()
        print("Camera error:")
        print(error)

    finally:

        # ---------------------------------------------------
        # Cleanup
        # ---------------------------------------------------

        sender.disconnect()

        camera.stop()

        cv2.destroyAllWindows()

        print()
        print("CleanWatch camera client stopped.")


if __name__ == "__main__":
    main()