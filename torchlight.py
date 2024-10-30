import torch
import cv2
from ultralytics import YOLO  # Ensure correct YOLO model import

# Load the YOLO model (replace with your specific model if necessary)
model = YOLO('best_5k.pt').to('cuda')  # Load and move to CUDA


# Open the video file
video_source = 'cash1.mp4'
cap = cv2.VideoCapture(video_source)
# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total number of frames in the video: ", total_frames)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    while cap.isOpened():
        ret, frame = cap.read()  # Read a frame
        if not ret:
            break  # Break if end of video is reached

        # Perform inference on the frame (ensure correct method is used for your YOLO version)
        results = model(frame, device=1)  # Optionally specify device if required

        # Process the results as needed (for now, no output is needed)

# Release the video capture object
cap.release()
