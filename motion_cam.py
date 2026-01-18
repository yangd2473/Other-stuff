from picamera2 import Picamera2
import cv2
import numpy as np
import time
from datetime import datetime
import os

SAVE_DIR = "/home/compooder/surveillance/videos"
os.makedirs(SAVE_DIR, exist_ok=True)

MOTION_THRESHOLD = 4000  # number of changed pixels to trigger motion
STOP_DELAY = 5  # seconds to wait after last motion to stop recording
FRAME_WIDTH, FRAME_HEIGHT = 1280, 720
FPS = 30

picam2 = Picamera2()
video_config = picam2.create_video_configuration(
    main={"size": (FRAME_WIDTH, FRAME_HEIGHT), "format": "RGB888"},
    controls={"FrameRate": FPS})
picam2.configure(video_config)
picam2.start()
time.sleep(2)  # allow camera to warm up

prev_gray = None
recording = False
last_motion_time = 0
video_writer = None

print("Motion surveillance running...")

while True:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if prev_gray is None:
        prev_gray = gray
        continue

    delta = cv2.absdiff(prev_gray, gray)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    motion_pixels = cv2.countNonZero(thresh)
    now = time.time()

    if motion_pixels > MOTION_THRESHOLD:
        last_motion_time = now
        if not recording:
            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.mp4")
            filepath = os.path.join(SAVE_DIR, filename)
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            video_writer = cv2.VideoWriter(filepath, fourcc, FPS, (FRAME_WIDTH, FRAME_HEIGHT))
            recording = True
            print(f"Recording started: {filename}")

    if recording:
        video_writer.write(frame)
        if now - last_motion_time > STOP_DELAY:
            video_writer.release()
            video_writer = None
            recording = False
            print("Recording stopped")

    prev_gray = gray
