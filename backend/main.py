"""
CleanWatch AI - Main AI Server

Current pipeline:

Camera
   ↓
Frame Receiver
   ↓
AI Processing Layer
   ↓
Control Room

YOLO, tracking, identity and event detection
will be connected to the processing section later.
"""

import asyncio
import time

import cv2
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import StreamingResponse

from backend.camera_stream import camera_manager


app = FastAPI(
    title="CleanWatch AI",
    description="AI-Based Littering Event Detection System",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "system": "CleanWatch AI",
        "status": "running",
        "service": "AI Server"
    }


@app.get("/camera/status")
def camera_status():

    return camera_manager.get_status()


@app.post("/camera/frame")
async def receive_camera_frame(
    camera_id: str = Form(...),
    frame: UploadFile = File(...)
):

    image_bytes = await frame.read()

    # Convert JPEG bytes to OpenCV image
    image_array = __import__("numpy").frombuffer(
        image_bytes,
        dtype=__import__("numpy").uint8
    )

    image = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )

    if image is None:
        return {
            "success": False,
            "message": "Invalid image received"
        }

    # Store frame
    camera_manager.update_frame(
        image,
        camera_id
    )

    # -------------------------------------------------------
    # FUTURE AI PIPELINE
    # -------------------------------------------------------
    #
    # detections = person_detector.detect(image)
    #
    # tracked_people = tracker.update(detections)
    #
    # identities = identity_matcher.identify(...)
    #
    # events = littering_detector.process(...)
    #
    # decision = decision_engine.evaluate(...)
    #
    # -------------------------------------------------------

    return {
        "success": True,
        "camera_id": camera_id
    }


def generate_video():

    while True:

        frame = camera_manager.get_frame()

        if frame is None:

            # No camera frame yet
            time.sleep(0.1)
            continue

        # Convert OpenCV frame → JPEG
        success, encoded = cv2.imencode(
            ".jpg",
            frame
        )

        if not success:
            continue

        jpeg = encoded.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + jpeg
            + b"\r\n"
        )

        time.sleep(0.03)


@app.get("/camera/video")
def camera_video():

    return StreamingResponse(
        generate_video(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )