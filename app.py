import gradio as gr
import numpy as np
import cv2

def process_webcam_image(image):
    # gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    gray_image = image
    return gray_image

iface = gr.Interface(
    fn=process_webcam_image,
    inputs=gr.Image(source="webcam", streaming=True), 
    live=True,
    outputs="image",
    title="Real-time Webcam Grayscale",
    description="This demo converts your webcam feed to grayscale in real-time."
)

iface.launch()
