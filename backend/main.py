
import threading
import time
from datetime import datetime, timezone

import cv2
import numpy as np
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

from backend.camera_stream import camera_manager


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = (
    r"E:\Littering_event_detection"
    r"\outputs\waste_detection-3"
    r"\weights\best.pt"
)

PERSON_MODEL_PATH = r"E:\Littering_event_detection\yolo11n.pt"

CONFIDENCE_THRESHOLD = 0.25
FRAME_WAIT_SECONDS = 0.01

app = FastAPI(title="CleanWatch AI")


# ============================================================
# LOAD MODELS
# ============================================================

print("Loading CleanWatch AI models...")

model = YOLO(MODEL_PATH)
person_model = YOLO(PERSON_MODEL_PATH)

print("Waste detection model loaded.")
print("Person detection model loaded.")


# ============================================================
# SHARED STATE
# ============================================================

ai_lock = threading.Lock()
latest_ai_frame = None
latest_camera_id = None

detections_lock = threading.Lock()

latest_detections = {
    "frame": 0,
    "timestamp_utc": None,
    "camera_id": None,
    "persons": [],
    "waste": [],
    "processing_error": None,
}

detection_frame_number = 0

annotated_lock = threading.Lock()
latest_annotated_frame = None

ai_running = True
ai_thread = None


# ============================================================
# FRAME INPUT
# ============================================================

def update_ai_frame(frame, camera_id="camera_1"):
    """Store the latest camera frame for AI processing."""
    global latest_ai_frame, latest_camera_id

    if frame is None:
        return

    with ai_lock:
        latest_ai_frame = frame.copy()
        latest_camera_id = camera_id


# ============================================================
# DETECTION EXTRACTION
# ============================================================

def extract_objects(results, class_names):
    """Convert YOLO results into JSON-compatible detection records."""
    objects = []

    if not results:
        return objects

    result = results[0]

    if result.boxes is None:
        return objects

    for box in result.boxes:
        xyxy = box.xyxy[0].cpu().tolist()

        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())

        track_id = None

        if box.id is not None:
            track_id = int(box.id[0].item())

        if isinstance(class_names, dict):
            class_name = class_names.get(class_id, str(class_id))
        elif isinstance(class_names, (list, tuple)):
            class_name = (
                class_names[class_id]
                if class_id < len(class_names)
                else str(class_id)
            )
        else:
            class_name = str(class_id)

        objects.append(
            {
                "track_id": track_id,
                "class_id": class_id,
                "class_name": class_name,
                "confidence": round(confidence, 4),
                "bbox": [round(float(value), 2) for value in xyxy],
            }
        )

    return objects


# ============================================================
# AI PROCESSING LOOP
# ============================================================

def ai_processing_loop():
    """
    Process the newest available frame.

    The loop takes the latest frame rather than building a queue
    of old frames, helping keep live monitoring responsive.
    """
    global detection_frame_number
    global latest_annotated_frame

    print("AI processing loop started.")

    while ai_running:
        with ai_lock:
            frame = (
                latest_ai_frame.copy()
                if latest_ai_frame is not None
                else None
            )
            camera_id = latest_camera_id

        if frame is None:
            time.sleep(0.1)
            continue

        try:
            # Waste detection and tracking
            waste_results = model.track(
                source=frame,
                conf=CONFIDENCE_THRESHOLD,
                persist=True,
                verbose=False,
            )

            # Person detection and tracking
            person_results = person_model.track(
                source=frame,
                conf=CONFIDENCE_THRESHOLD,
                persist=True,
                classes=[0],
                verbose=False,
            )

            waste_objects = extract_objects(
                waste_results,
                model.names,
            )

            person_objects = extract_objects(
                person_results,
                person_model.names,
            )

            timestamp = datetime.now(timezone.utc).isoformat()

            with detections_lock:
                detection_frame_number += 1

                latest_detections.update(
                    {
                        "frame": detection_frame_number,
                        "timestamp_utc": timestamp,
                        "camera_id": camera_id,
                        "persons": person_objects,
                        "waste": waste_objects,
                        "processing_error": None,
                    }
                )

            # Annotate frame with waste detections
            annotated_frame = frame.copy()

            if waste_results:
                annotated_frame = waste_results[0].plot(
                    img=annotated_frame
                )

            # Overlay person detections
            if person_results:
                annotated_frame = person_results[0].plot(
                    img=annotated_frame
                )

            with annotated_lock:
                latest_annotated_frame = annotated_frame.copy()

            # Send annotated frames to the existing camera manager.
            # If its API differs in your project, adjust this call
            # to match backend/camera_stream.py.
            try:
                camera_manager.update_frame(annotated_frame)
            except (AttributeError, TypeError):
                pass

        except Exception as exc:
            error_message = f"{type(exc).__name__}: {exc}"
            print(f"AI processing error: {error_message}")

            with detections_lock:
                latest_detections["processing_error"] = error_message

            time.sleep(0.1)

        time.sleep(FRAME_WAIT_SECONDS)

    print("AI processing loop stopped.")


# ============================================================
# STARTUP AND SHUTDOWN
# ============================================================

@app.on_event("startup")
def startup_event():
    global ai_thread, ai_running

    ai_running = True

    if ai_thread is None or not ai_thread.is_alive():
        ai_thread = threading.Thread(
            target=ai_processing_loop,
            daemon=True,
            name="CleanWatchAIProcessing",
        )
        ai_thread.start()


@app.on_event("shutdown")
def shutdown_event():
    global ai_running

    ai_running = False

    if ai_thread is not None and ai_thread.is_alive():
        ai_thread.join(timeout=3)


# ============================================================
# ROOT / HEALTH CHECK
# ============================================================

@app.get("/")
def root():
    return {
        "project": "CleanWatch AI",
        "status": "running",
        "ai_processing": ai_thread is not None and ai_thread.is_alive(),
        "endpoints": [
            "/",
            "/camera/frame",
            "/camera/status",
            "/camera/video",
            "/ai/detections",
        ],
    }


# ============================================================
# CAMERA FRAME UPLOAD
# ============================================================

@app.post("/camera/frame")
async def receive_camera_frame(
    frame: UploadFile = File(...),
    camera_id: str = Form("camera_1"),
):
    """
    Receive a JPEG image from camera/frame_sender.py.

    IMPORTANT:
    The upload field is named 'frame' to match the client request.
    """
    contents = await frame.read()

    if not contents:
        return {
            "status": "error",
            "message": "Empty image upload",
        }

    image_array = np.frombuffer(contents, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        return {
            "status": "error",
            "message": "Invalid image data",
        }

    update_ai_frame(image, camera_id)

    return {
        "status": "received",
        "camera_id": camera_id,
        "width": int(image.shape[1]),
        "height": int(image.shape[0]),
    }


# ============================================================
# AI DETECTIONS API
# ============================================================

@app.get("/ai/detections")
def get_ai_detections():
    with detections_lock:
        return dict(latest_detections)


# ============================================================
# CAMERA STATUS API
# ============================================================

@app.get("/camera/status")
def get_camera_status():
    with ai_lock:
        frame_available = latest_ai_frame is not None
        camera_id = latest_camera_id

    with detections_lock:
        detection_snapshot = dict(latest_detections)

    thread_alive = ai_thread is not None and ai_thread.is_alive()

    return {
        "camera_connected": frame_available,
        "camera_id": camera_id,
        "ai_processing": thread_alive,
        "latest_detection_frame": detection_snapshot["frame"],
        "last_processed_timestamp_utc": (
            detection_snapshot["timestamp_utc"]
        ),
        "processing_error": detection_snapshot["processing_error"],
    }


# ============================================================
# ANNOTATED VIDEO STREAM
# ============================================================

def generate_ai_frames():
    """Yield annotated frames as an MJPEG stream."""
    while True:
        with annotated_lock:
            frame = (
                latest_annotated_frame.copy()
                if latest_annotated_frame is not None
                else None
            )

        if frame is None:
            time.sleep(0.1)
            continue

        success, encoded = cv2.imencode(".jpg", frame)

        if not success:
            time.sleep(0.05)
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + encoded.tobytes()
            + b"\r\n"
        )

        time.sleep(0.03)


@app.get("/camera/video")
def camera_video():
    return StreamingResponse(
        generate_ai_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )