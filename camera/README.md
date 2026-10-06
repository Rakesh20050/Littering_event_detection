# CleanWatch AI Camera Module

This folder handles camera input for the CleanWatch AI system.

## Current Architecture

Camera
   ↓
OpenCV
   ↓
VideoStream
   ↓
camera_client.py
   ↓
Live preview


## Supported Camera Sources

### 1. Laptop Webcam

In `camera_config.py`:

```python
CAMERA_SOURCE = 0