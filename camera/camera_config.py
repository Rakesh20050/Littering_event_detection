"""
CleanWatch AI - Camera Configuration
"""

# -------------------------------------------------------
# CAMERA SOURCE
# -------------------------------------------------------

# Phone camera using IP Webcam
CAMERA_SOURCE = "http://130.1.8.118:8080/video"


# Unique camera identifier
CAMERA_ID = "CAMERA_01"


# -------------------------------------------------------
# AI SERVER
# -------------------------------------------------------

# FastAPI is running on the same laptop
AI_SERVER_URL = "http://127.0.0.1:8000"


# -------------------------------------------------------
# RESOLUTION
# -------------------------------------------------------

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720


# -------------------------------------------------------
# LOCAL PREVIEW
# -------------------------------------------------------

SHOW_PREVIEW = True