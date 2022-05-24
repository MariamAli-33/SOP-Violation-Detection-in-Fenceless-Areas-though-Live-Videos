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
def sd_detection_image():
    results=[]
    confidence_threshold = 0.3
    score_threshold = 0.5
    iou_threshold = 0.5
    safe_distance=350
    config_path = 'yolov4(b).cfg'
    weights_path = 'yolov4.weights'
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) 
    ln = net.getLayerNames()
    ln = [ln[i-1] for i in net.getUnconnectedOutLayers()]
    st.title('Social Distancing Detection using Images')
    st.write("""
    The application takes an image as input and returns an image with the detection of maintenance of Social Distance between individuals. The red bounding box indicates the violation of SOP and the Green bounding box represents the safe distance. The user is instructed to wait as the model processing depends on file size. Users can download the detected results as well.
    """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])
    if file!= None:
        img1 = Image.open(file)
        img2 = np.array(img1)
        st.image(img1, caption = "Uploaded Image")
        my_bar = st.progress(0)
        LABELS_FILE='coco.names'
        LABELS = open(LABELS_FILE).read().strip().split("\n")
        np.random.seed(4)
        def detect_people(outputs, image, personIdx=0):
            nms_threshold=0.3
            (H, W) = image.shape[:2]
            results = []
            blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),swapRB=True, crop=False)
            net.setInput(blob)
            layerOutputs = net.forward(ln)
            boxes = []
            centroids = []
            confidences = []
            for output in layerOutputs:
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    if classID == personIdx and confidence > 0.3:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        centroids.append((centerX, centerY))
                        confidences.append(float(confidence))
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
            if len(idxs) > 0:
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    r = (confidences[i], (x, y, x + w, y + h), centroids[i])
                    results.append(r)
            return results       
        blob = cv2.dnn.blobFromImage(img2, 1 / 255, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        outputs = net.forward(ln)
        boxes, confidences, class_ids, centroids = [],[], [], []
        results = detect_people(outputs, img2, personIdx=LABELS.index("person"))
        violate = set()
        if len(results) >= 2:
            centroids=np.array([r[2] for r in results])
            D = dist.cdist(centroids, centroids, metric="euclidean")
            for i in range(0, D.shape[0]):
                for j in range(i + 1, D.shape[1]):
                    if D[i, j] < safe_distance:
                        violate.add(i)
                        violate.add(j)
        for (i, (prob, bbox, centroid)) in enumerate(results):
            (startX, startY, endX, endY) = bbox
            (cX, cY) = centroid
            color = (0, 255, 0)
            if i in violate:
                color = (255, 0, 0)
            cv2.rectangle(img2, (startX, startY), (endX, endY), color, 2)
            cv2.circle(img2, (cX, cY), 5, color, 1)
        text = "Social Distancing Violations: {}".format(len(violate))
        cv2.putText(img2, text, (10, img2.shape[0] - 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255,0,0), 3)
        st.image(img2, caption='Proccesed Image.')
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
def detect_people(frame, net, ln, personIdx=0):
    confidence_threshold=0.3
    nms_threshold=0.3
    (H, W) = frame.shape[:2]
    results = []
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    boxes = []
    centroids = []
    confidences = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if classID == personIdx and confidence > confidence_threshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                centroids.append((centerX, centerY))
                confidences.append(float(confidence))
                print(confidence)
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            r = (confidences[i], (x, y, x + w, y + h), centroids[i])
            results.append(r)
    return results
def sd_detection_video():
    results=[]
    confidence_threshold = 0.3
    score_threshold = 0.5
    iou_threshold = 0.5
    config_path= 'yolov4(b).cfg'
    weights_path = 'yolov4.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='coco.names'
    safe_distance=350
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    np.random.seed(4)
    colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    st.title("Social Distancing Detection using Videos")
    st.write("""
   The application takes a video as input and returns a video with the detection of maintenance of Social Distance between individuals. The red bounding box indicates the violation of SOP and the Green bounding box represents the safe distance. The user is instructed to wait as the model processing depends on file size. Users can download the detected results as well.
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
        out = cv2.VideoWriter("SDdetected_video.mp4", fourcc, 20.0, (w, h))
        count = 0
        my_bar = st.progress(0)
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
                print(f"Time took: {count}", time_took)
                boxes, confidences, class_ids, centroids = [],[], [], []
                results = detect_people(image, net, ln, personIdx=LABELS.index("person"))
                violate = set()
                if len(results) >= 2:
                    centroids=np.array([r[2] for r in results])
                    D = dist.cdist(centroids, centroids, metric="euclidean")
                    for i in range(0, D.shape[0]):
                        for j in range(i + 1, D.shape[1]):
                            if D[i, j] < safe_distance:
                                violate.add(i)
                                violate.add(j)
                for (i, (prob, bbox, centroid)) in enumerate(results):
                    (startX, startY, endX, endY) = bbox
                    (cX, cY) = centroid
                    color = (0, 255, 0)
                    if i in violate:
                        color = (0, 0, 255)
                    cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                    cv2.circle(image, (cX, cY), 5, color, 1)
                text = "Social Distancing Violations: {}".format(len(violate))
                cv2.putText(image, text, (10, image.shape[0] - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 3)
                out.write(image)
                cv2.imshow("image", image)
                
                if ord("q") == cv2.waitKey(1):
                    break
            else:
                break

                    
        cap.release()
        cv2.destroyAllWindows()
        my_bar.progress(100)
        return "SDdetected_video.mp4"


def sd_detection_live():
    results=[]
    confidence_threshold = 0.3
    score_threshold = 0.5
    iou_threshold = 0.5
    config_path= 'yolov4(b).cfg'
    weights_path = 'yolov4.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='coco.names'
    safe_distance=350
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    np.random.seed(4)
    colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    st.title("Social Distancing Detection using Live Stream")
    st.write("""
    The application processes Live stream and return a video with the detection of maintenance of Social Distance between individuals. The red bounding box indicates the violation of SOP and the Green bounding box represents the safe distance. The user is instructed to wait as the model processing depends on the availability of bandwidth. Users can download the detected results as well.
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
            out = cv2.VideoWriter("SDdetected_LiveVideo.mp4", fourcc, 20.0, (w, h))
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
                    boxes, confidences, class_ids, centroids = [],[], [], []
                    results = detect_people(image, net, ln, personIdx=LABELS.index("person"))
                    violate = set()
                    if len(results) >= 2:
                        centroids=np.array([r[2] for r in results])
                        D = dist.cdist(centroids, centroids, metric="euclidean")
                        for i in range(0, D.shape[0]):
                            for j in range(i + 1, D.shape[1]):
                                if D[i, j] < safe_distance:
                                    violate.add(i)
                                    violate.add(j)
                    for (i, (prob, bbox, centroid)) in enumerate(results):
                        (startX, startY, endX, endY) = bbox
                        (cX, cY) = centroid
                        color = (0, 255, 0)
                        if i in violate:
                            color = (0, 0, 255)
                        cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                        cv2.circle(image, (cX, cY), 5, color, 1)
                    text = "Social Distancing Violations: {}".format(len(violate))
                    cv2.putText(image, text, (10, image.shape[0] - 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 3)
                    out.write(image)
                    cv2.imshow("image", image)
                
                    if ord("q") == cv2.waitKey(1):
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
            return "SDdetected_LiveVideo.mp4"
            

def main():
    st.sidebar.header("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("Social Distancing Detection(Image)","Social Distancing Detection(Video)", "Social Distancing Detection(Live)"))
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
    
    if choice == "Social Distancing Detection(Image)":
        sd_detection_image()
    
    elif choice == "Social Distancing Detection(Video)":
        #object_detection_video.has_beenCalled = False
        sd_detection_video()
    
        #if object_detection_video.has_beenCalled:
        try:
            clip = moviepy.VideoFileClip('SDdetected_video.mp4')
            clip.write_videofile("SDvideo.mp4")
            st_video = open('SDvideo.mp4','rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Detected Video") 
            st.markdown(get_binary_file_downloader_html('SDVideo.mp4', 'Video'), unsafe_allow_html=True)
        except OSError:
            ''
    elif choice == "Social Distancing Detection(Live)":
        sd_detection_live()
        try:
            clip = moviepy.VideoFileClip('SDdetected_LiveVideo.mp4')
            clip.write_videofile("SDvideoLive.mp4")
            st_video = open('SDvideoLive.mp4','rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Detected Video") 
            st.markdown(get_binary_file_downloader_html('SDvideoLive.mp4', 'Video'), unsafe_allow_html=True)
        except OSError:
            ''

if __name__ == '__main__':
		main()	