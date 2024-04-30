import streamlit as st
import cv2
import numpy as np
import os

def add_watermark(video_path, image_path, output_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    
    # Load the watermark image
    watermark = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    (wH, wW) = watermark.shape[:2]
    
    # Resize watermark to be 10% of the video's width
    scale_factor = frame_width * 0.1 / wW
    watermark = cv2.resize(watermark, (0, 0), fx=scale_factor, fy=scale_factor)
    (wH, wW) = watermark.shape[:2]

    # Setting watermark position
    overlay_x = frame_width - wW - 10  # 10 pixels from the right
    overlay_y = frame_height - wH - 10  # 10 pixels from the bottom

    # Process each frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Add the watermark
        overlay = frame.copy()
        overlay[overlay_y:overlay_y+wH, overlay_x:overlay_x+wW] = cv2.addWeighted(overlay[overlay_y:overlay_y+wH, overlay_x:overlay_x+wW], 0.5, watermark, 0.5, 0)

        # Write the frame with the watermark
        out.write(overlay)

    cap.release()
    out.release()



st.title('Video Watermarking App')
# Add the footnote at the end of your Streamlit app
st.markdown('This application creates a new video file with the given image as a watermark. The watermark will be placed in the bottom right corner of the video.')


video_file = st.file_uploader("Choose a video...", type=["mp4"])
image_file = st.file_uploader("Choose an image for watermark...", type=["png", "jpg"])

if video_file and image_file:
    video_path = video_file.name
    image_path = image_file.name
    output_path = "watermarked_output.mp4"

    with open(video_path, "wb") as f:
        f.write(video_file.getbuffer())
        
    with open(image_path, "wb") as f:
        f.write(image_file.getbuffer())

    if st.button('Process Video'):
            add_watermark(video_path, image_path, output_path)
            st.success('Processing Complete!')
            st.text(f'New video was saved to: {os.path.realpath(output_path)}')

# Add the footnote at the end of your Streamlit app
st.markdown('---')
st.markdown('Created by [Johannes Hayer](https://jhayer.tech) - Software Engineer')