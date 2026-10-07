"""
CleanWatch AI - Main AI Server

Pipeline:

Phone Camera
    ↓
Camera Client
    ↓
FastAPI
    ↓
Latest Frame Buffer
    ↓
YOLO Detection Thread
    ↓
Annotated Frame
    ↓
Control Room
"""

import threading
import time

import cv2
import numpy as np
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

from backend.camera_stream import camera_manager


# =========================================================
# FASTAPI
# =========================================================

app = FastAPI(
    title="CleanWatch AI",
    description="AI-Based Littering Event Detection System",
    version="1.0.0"
)


# =========================================================
# YOLO MODEL
# =========================================================

MODEL_PATH = (
    r"E:\Littering_event_detection"
    r"\outputs\waste_detection-3"
    r"\weights\best.pt"
)

print()
print("=" * 60)
print("Loading CleanWatch AI YOLO model...")
print("=" * 60)

model = YOLO(MODEL_PATH)

print("YOLO model loaded successfully.")
print("Classes:", model.names)
print("=" * 60)
print()


# =========================================================
# AI FRAME BUFFER
# =========================================================

ai_lock = threading.Lock()

latest_ai_frame = None
latest_camera_id = None

ai_running = True


# =========================================================
# STORE FRAME FOR AI
# =========================================================

def update_ai_frame(frame, camera_id):

    global latest_ai_frame
    global latest_camera_id

    with ai_lock:

        # Replace old frame with newest frame.
        # Old frames are intentionally discarded.
        latest_ai_frame = frame
        latest_camera_id = camera_id


# =========================================================
# YOLO PROCESSING THREAD
# =========================================================

def ai_processing_loop():

    global latest_ai_frame
    global latest_camera_id

    print("AI processing thread started.")

    while ai_running:

        frame = None
        camera_id = None

        # -------------------------------------------------
        # Get newest frame
        # -------------------------------------------------

        with ai_lock:

            if latest_ai_frame is not None:

                frame = latest_ai_frame
                camera_id = latest_camera_id

                # Remove it from buffer.
                latest_ai_frame = None

        # -------------------------------------------------
        # No frame available
        # -------------------------------------------------

        if frame is None:

            time.sleep(0.01)
            continue

        # -------------------------------------------------
        # YOLO detection
        # -------------------------------------------------

        try:

            results = model.predict(
                source=frame,
                conf=0.25,
                verbose=False
            )

            annotated_frame = results[0].plot()

            # -------------------------------------------------
            # Send annotated frame to Control Room buffer
            # -------------------------------------------------

            camera_manager.update_frame(
                annotated_frame,
                camera_id
            )

        except Exception as error:

            print("YOLO processing error:", error)

            # Keep original frame available if AI fails.
            camera_manager.update_frame(
                frame,
                camera_id
            )


# =========================================================
# START AI THREAD
# =========================================================

ai_thread = threading.Thread(
    target=ai_processing_loop,
    daemon=True
)

ai_thread.start()


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    return {
        "system": "CleanWatch AI",
        "status": "running",
        "service": "AI Server"
    }


# =========================================================
# CAMERA STATUS
# =========================================================

@app.get("/camera/status")
def camera_status():

    return camera_manager.get_status()


# =========================================================
# RECEIVE CAMERA FRAME
# =========================================================

@app.post("/camera/frame")
async def receive_camera_frame(
    camera_id: str = Form(...),
    frame: UploadFile = File(...)
):

    image_bytes = await frame.read()

    image_array = np.frombuffer(
        image_bytes,
        dtype=np.uint8
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

    # -----------------------------------------------------
    # Store newest frame for AI processing.
    #
    # IMPORTANT:
    # The API does NOT wait for YOLO.
    # -----------------------------------------------------

    update_ai_frame(
        image,
        camera_id
    )

    return {
        "success": True,
        "camera_id": camera_id
    }


# =========================================================
# LIVE VIDEO GENERATOR
# =========================================================

def generate_video():

    while True:

        frame = camera_manager.get_frame()

        if frame is None:

            time.sleep(0.05)
            continue

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


# =========================================================
# CAMERA VIDEO
# =========================================================

@app.get("/camera/video")
def camera_video():

    return StreamingResponse(
        generate_video(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )