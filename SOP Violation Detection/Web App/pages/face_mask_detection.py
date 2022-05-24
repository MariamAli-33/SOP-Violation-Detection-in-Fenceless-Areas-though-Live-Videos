import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import datetime
import cv2
from PIL import Image, ImageEnhance
import os
import time ,sys
from streamlit_embedcode import github_gist
import urllib.request
import urllib
import moviepy.editor as moviepy
import time
import sys
from itertools import combinations
import imutils
from imutils.video import FPS
from imutils.video import VideoStream
from scipy.spatial import distance as dist
import argparse
import base64
from io import BytesIO
def faceMask_detection_image():
    confidence_threshold = 0.3
    config_path = 'yolov4.cfg'
    weights_path = 'yolov4_best.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='classes.names'
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    np.random.seed(4)
    colors=[(0,255,0),(255,0,0)]
    #colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    st.title('Face Mask Detection using Images')
    st.write("""
    The application takes an image as input and returns an image with the intended area of the face detected as with a mask or not. The red bounding box indicates the No-Mask and the Green bounding box represents a person with Mask. The user is instructed to wait as the model processing depends on file size. Users can download the detected results as well.
    """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])
    if file!= None:
        img1 = Image.open(file)
        img2 = np.array(img1)
        st.image(img1, caption = "Uploaded Image")
        my_bar = st.progress(0)
        h, w = img2.shape[:2]
        blob = cv2.dnn.blobFromImage(img2, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        layer_outputs = net.forward(ln)
        boxes, confidences, class_ids = [], [], []
        for output in layer_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > confidence_threshold:
                    box = detection[:4] * np.array([w, h, w, h])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, confidence_threshold)
        font_scale = 0.6
        thickness = 1
        if len(idxs) > 0:
            for i in idxs.flatten():
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                color = [int(c) for c in colors[class_ids[i]]]
                cv2.rectangle(img2, (x, y), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(LABELS[class_ids[i]], confidences[i])
                cv2.putText(img2, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color,2)
        st.image(img2, caption='Proccesed Image for Mask.')
        result = Image.fromarray(img2)
        st.markdown(get_image_download_link(result), unsafe_allow_html=True)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        my_bar.progress(100)
def get_image_download_link(img):
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}" download ="result.jpg">Download result</a>'
	return href
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href
def faceMask_detection_video():
    confidence_threshold= 0.3
    config_path = 'yolov4.cfg'
    weights_path = 'yolov4_4000.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='classes.names'
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    np.random.seed(4)
    colors=[(0,255,0),(255,0,0)]
    #colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    st.title("Face Mask Detection using Videos")
    st.write("""
    The application takes a video as input and returns a video with the intended area of the face detected as with a mask or not. The red bounding box indicates the No-Mask and the Green bounding box represents a person with Mask. The user is instructed to wait as the model processing depends on file size. Users can download the detected results as well.
    """
    )
    uploaded_video = st.file_uploader("Upload Video", type = ['mp4','mpeg','mov'])
    if uploaded_video != None:
        vid = uploaded_video.name
        with open(vid, mode='wb') as f:
            f.write(uploaded_video.read()) # save video to disk
        st_video = open(vid,'rb')
        video_bytes = st_video.read()
        st.video(video_bytes)
        st.write("Uploaded Video")
        cap = cv2.VideoCapture(vid)
        _, image = cap.read()
        h, w = image.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mpv4')
        out = cv2.VideoWriter("Maskdetected_video.mp4", fourcc, 20.0, (w, h))
        count = 0
        my_bar = st.progress(0)
        while True:
            _, image = cap.read()
            if _ != False:
                # for percent_complete in range(100):
                #     time.sleep(0.1)
                #     my_bar.progress(percent_complete + 1)
                h, w = image.shape[:2]
                blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
                net.setInput(blob)
                start = time.perf_counter()
                layer_outputs = net.forward(ln)
                time_took = time.perf_counter() - start
                count +=1
                #print(f"Time took: {count}", time_took)
                boxes, confidences, class_ids = [], [], []
                for output in layer_outputs:
                    for detection in output:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > confidence_threshold:
                            box = detection[:4] * np.array([w, h, w, h])
                            (centerX, centerY, width, height) = box.astype("int")
                            x = int(centerX - (width / 2))
                            y = int(centerY - (height / 2))
                            boxes.append([x, y, int(width), int(height)])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)
                idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, confidence_threshold)
                font_scale = 0.6
                thickness = 1
                if len(idxs) > 0:
                    for i in idxs.flatten():
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        color = [int(c) for c in colors[class_ids[i]]]
                        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                        text = "{}: {:.4f}".format(LABELS[class_ids[i]], confidences[i])
                        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
                out.write(image)
                cv2.imshow("image", image)

                if ord("q") == cv2.waitKey(1):
                    break
            else:
                break    
        
        cap.release()
        cv2.destroyAllWindows()
        my_bar.progress(100)
        return "Maskdetected_video.mp4"
def faceMask_detection_live():
    confidence_threshold= 0.3
    config_path = 'yolov4.cfg'
    weights_path = 'yolov4_4000.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='classes.names'
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    np.random.seed(4)
    colors=[(0,255,0),(255,0,0)]
    #colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    st.title("Face Mask Detection using Live Stream")
    st.write("""
    The application processes live camera footage and return a video with the intended area of the face detected as with a mask or not. The red bounding box indicates the No-Mask and the Green bounding box represents a person with Mask. The user is instructed to wait as the model processing depends on the availability of bandwidth. Users can download the detected results as well.
    """
    )
    videoType = st.radio(
     "What is the type of camera being used",
     ('Web Cam', 'Other Camera'))
    if videoType== 'Web Cam':
        url=0
    else:
        url = st.text_input('Camera Url with an extension of /video', "https://ip/video")
    cap = cv2.VideoCapture(url)

    if cap != None:
        _, image = cap.read()
        if image is None:
            st.write("No camera is found")
        else:
            h, w = image.shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*'mpv4')
            out = cv2.VideoWriter("Maskdetected_LiveVideo.mp4", fourcc, 20.0, (w, h))
            count = 0
            while True:
                _, image = cap.read()
                if _ != False:
                    h, w = image.shape[:2]
                    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
                    net.setInput(blob)
                    start = time.perf_counter()
                    layer_outputs = net.forward(ln)
                    time_took = time.perf_counter() - start
                    count +=1
                    #print(f"Time took: {count}", time_took)
                    boxes, confidences, class_ids = [], [], []
                    for output in layer_outputs:
                        for detection in output:
                            scores = detection[5:]
                            class_id = np.argmax(scores)
                            confidence = scores[class_id]
                            if confidence > confidence_threshold:
                                box = detection[:4] * np.array([w, h, w, h])
                                (centerX, centerY, width, height) = box.astype("int")
                                x = int(centerX - (width / 2))
                                y = int(centerY - (height / 2))
                                boxes.append([x, y, int(width), int(height)])
                                confidences.append(float(confidence))
                                class_ids.append(class_id)
                    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, confidence_threshold)
                    font_scale = 0.6
                    thickness = 1
                    if len(idxs) > 0:
                        for i in idxs.flatten():
                            (x, y) = (boxes[i][0], boxes[i][1])
                            (w, h) = (boxes[i][2], boxes[i][3])
                            color = [int(c) for c in colors[class_ids[i]]]
                            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                            text = "{}: {:.4f}".format(LABELS[class_ids[i]], confidences[i])
                            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
    
                    out.write(image)
                    cv2.imshow("image", image)
                
                    if ord("q") == cv2.waitKey(1):
                        break
                else:
                    break    
            cap.release()
            cv2.destroyAllWindows()
            
        return "Maskdetected_LiveVideo"
def main():
    st.sidebar.header("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("Face Mask Detection(Image)","Face Mask Detection(Video)","Face Mask Detection(Live)"))

    if choice == "Face Mask Detection(Image)":
        faceMask_detection_image()

    elif choice == "Face Mask Detection(Video)":
        faceMask_detection_video()
        try:

            clip = moviepy.VideoFileClip('Maskdetected_video.mp4')
            clip.write_videofile("MaskVideo.mp4")
            st_video = open('MaskVideo.mp4','rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Detected Video") 
            st.markdown(get_binary_file_downloader_html('MaskVideo.mp4', 'Video'), unsafe_allow_html=True) 
        except OSError:
            ''
    elif choice == "Face Mask Detection(Live)":
        faceMask_detection_live()
        try:
            clip = moviepy.VideoFileClip('Maskdetected_LiveVideo.mp4')
            clip.write_videofile("MaskVideoLive.mp4")
            st_video = open('MaskVideoLive.mp4','rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Detected Video") 
            st.markdown(get_binary_file_downloader_html('MaskVideoLive.mp4', 'Video'), unsafe_allow_html=True) 
        except OSError:
            ''        
         

if __name__ == '__main__':
		main()	