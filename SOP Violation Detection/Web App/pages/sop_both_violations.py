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
            if classID == personIdx and confidence > MIN_CONF:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                centroids.append((centerX, centerY))
                confidences.append(float(confidence))
                print(confidence)
    idxs = cv2.dnn.NMSBoxes(boxes, confidences,confidence_threshold, nms_threshold)
    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            r = (confidences[i], (x, y, x + w, y + h), centroids[i])
            results.append(r)
    return results
def both_detection_live():
    results=[]
    confidence_threshold= 0.3
    score_threshold = 0.5
    iou_threshold= 0.5
    config_path = 'yolov4.cfg'
    weights_path = 'yolov4_4000.weights'
    config_path1 = 'yolov4(b).cfg'
    weights_path1 = 'yolov4.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='classes.names'
    LABELS_FILE1='coco.names'
    safe_distance=450
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    LABELS1 = open(LABELS_FILE1).read().strip().split("\n")
    np.random.seed(4)
    colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    colors1 = np.random.randint(0, 255, size=(len(LABELS1), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    net1 = cv2.dnn.readNetFromDarknet(config_path1, weights_path1)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    ln1 = net1.getLayerNames()
    ln1 = [ln1[i - 1] for i in net1.getUnconnectedOutLayers()]
    st.title("SOPs(both) Detection using Live Stream")
    st.write("""
    The application processes Live stream and return a video with the detection of the Face Mask and maintenance of Social Distance between individuals. The red bounding box indicates the violation of SOP and the Green bounding box represents the abidance. The user is instructed to wait as the model processing depends on the availability of bandwidth. Users can download the detected results as well.
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
            out = cv2.VideoWriter("BothDetected_LiveVideo.mp4", fourcc, 20.0, (w, h))
            count = 0
            while True:
                _, image = cap.read()
                if _ != False:
                    h, w = image.shape[:2]
                    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
                    net.setInput(blob)
                    net1.setInput(blob)
                    start = time.perf_counter()
                    layer_outputs = net.forward(ln)
                    layer_outputs1 = net1.forward(ln1)
                    time_took = time.perf_counter() - start
                    count +=1
                #print(f"Time took: {count}", time_took)
                    boxes, confidences, class_ids = [], [], []
                    boxes1, confidences1, class_ids1, centroids = [],[], [], []
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
                    idxs = cv2.dnn.NMSBoxes(boxes, confidences,confidence_threshold ,confidence_threshold )
                    if len(idxs) > 0:
                        for i in idxs.flatten():
                            (x, y) = (boxes[i][0], boxes[i][1])
                            (w, h) = (boxes[i][2], boxes[i][3])
                            color = [int(c) for c in colors[class_ids[i]]]
                            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                            text = "{}: {:.4f}".format(LABELS[class_ids[i]], confidences[i])
                            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
                    results = detect_people(image, net1, ln1, personIdx=LABELS1.index("person"))
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
            return "BothDetected_LiveVideo"
            

def both_detection_image():
    results=[]
    confidence_threshold = 0.3
    nms_threshold=0.3
    score_threshold = 0.5
    iou_threshold = 0.5
    safe_distance=450
    config_path = 'yolov4.cfg'
    weights_path = 'yolov4_best.weights'
    config_path1 = 'yolov4(b).cfg'
    weights_path1 = 'yolov4.weights'
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) 
    ln = net.getLayerNames()
    ln = [ln[i-1] for i in net.getUnconnectedOutLayers()]
    net1 = cv2.dnn.readNetFromDarknet(config_path1, weights_path1)
    net1.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net1.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) 
    ln1 = net1.getLayerNames()
    ln1 = [ln1[i-1] for i in net1.getUnconnectedOutLayers()]
    st.title('SOPs(both) Detection using Images')
    st.write("""
    The application takes an image as input and returns an image with the detection of the Face Mask and maintenance of Social Distance between individuals. The red bounding box indicates the violation of SOP and the Green bounding box represents the abidance. The user is instructed to wait as the model processing depends on file size. Users can download the detected results as well.
    """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])
    if file!= None:
        img1 = Image.open(file)
        img2 = np.array(img1)
        st.image(img1, caption = "Uploaded Image")
        h, w = img2.shape[:2]
        my_bar = st.progress(0)
        LABELS_FILE='classes.names'
        LABELS = open(LABELS_FILE).read().strip().split("\n")
        LABELS_FILE1='coco.names'
        LABELS1 = open(LABELS_FILE1).read().strip().split("\n")
        colors=[(0,255,0),(255,0,0)]
        # colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
        colors1 = np.random.randint(0, 255, size=(len(LABELS1), 3), dtype="uint8")
        np.random.seed(4)
        def detect_people(image,net,ln, personIdx=0):
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
                    if classID == personIdx and confidence >confidence_threshold:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        centroids.append((centerX, centerY))
                        confidences.append(float(confidence))
                        #print(confidence)
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
        net1.setInput(blob)
        layer_outputs = net.forward(ln)
        layer_outputs1 = net1.forward(ln1)
        boxes, confidences, class_ids= [],[], []
        boxes1, confidences1, class_ids1, centroids1 = [],[], [], []
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
        results = detect_people(img2,net1,ln1, personIdx=LABELS1.index("person"))
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
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, confidence_threshold)
    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            r = (confidences[i], (x, y, x + w, y + h), centroids[i])
            results.append(r)
    return results
def both_detection_video():
    results=[]
    confidence_threshold= 0.3
    score_threshold = 0.5
    iou_threshold = 0.5
    config_path = 'yolov4.cfg'
    weights_path = 'yolov4_4000.weights'
    config_path1 = 'yolov4(b).cfg'
    weights_path1 = 'yolov4.weights'
    font_scale = 1
    thickness = 1
    LABELS_FILE='classes.names'
    LABELS_FILE1='coco.names'
    safe_distance=450
    LABELS = open(LABELS_FILE).read().strip().split("\n")
    LABELS1 = open(LABELS_FILE1).read().strip().split("\n")
    np.random.seed(4)
    colors=[(0,255,0),(255,0,0)]
    # colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    colors1 = np.random.randint(0, 255, size=(len(LABELS1), 3), dtype="uint8")
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    net1 = cv2.dnn.readNetFromDarknet(config_path1, weights_path1)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
    ln1 = net1.getLayerNames()
    ln1 = [ln1[i - 1] for i in net1.getUnconnectedOutLayers()]
    st.title("SOPs(both) Detection using Videos")
    st.write("""
    The application takes a video as input and returns a video with the detection of the Face Mask and maintenance of Social Distance between individuals. The red bounding box indicates the violation of SOP and the Green bounding box represents the abidance. The user is instructed to wait as the model processing depends on file size. Users can download the detected results as well.
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
        out = cv2.VideoWriter("Bothdetected_video.mp4", fourcc, 20.0, (w, h))
        count = 0
        my_bar = st.progress(0)
        while True:
            _, image = cap.read()
            if _ != False:
                h, w = image.shape[:2]
                blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
                net.setInput(blob)
                net1.setInput(blob)
                start = time.perf_counter()
                layer_outputs = net.forward(ln)
                layer_outputs1 = net1.forward(ln1)
                time_took = time.perf_counter() - start
                count +=1
                print(f"Time took: {count}", time_took)
                boxes, confidences, class_ids = [], [], []
                boxes1, confidences1, class_ids1, centroids = [],[], [], []
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
                idxs = cv2.dnn.NMSBoxes(boxes, confidences,confidence_threshold,confidence_threshold)
                if len(idxs) > 0:
                    for i in idxs.flatten():
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        color = [int(c) for c in colors[class_ids[i]]]
                        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                        text = "{}: {:.4f}".format(LABELS[class_ids[i]], confidences[i])
                        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
                results = detect_people(image, net1, ln1, personIdx=LABELS1.index("person"))
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
        return "Bothdetected_video.mp4"
        


def main():
    st.sidebar.header("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("SOPs Detection(Image)","SOPs Detection(Video)","SOPs Detection(Live)"))
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
    
    if choice == "SOPs Detection(Image)":
        both_detection_image()
        
    
    elif choice == "SOPs Detection(Video)":
        both_detection_video()
    
        #if object_detection_video.has_beenCalled:
        try:
            clip = moviepy.VideoFileClip('Bothdetected_video.mp4')
            clip.write_videofile("Bothvideo.mp4")
            st_video = open('Bothvideo.mp4','rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Detected Video") 
            st.markdown(get_binary_file_downloader_html('Bothvideo.mp4', 'Video'), unsafe_allow_html=True)
        except OSError:
            ''

    elif choice == "SOPs Detection(Live)":
        both_detection_live()
        try:
            clip = moviepy.VideoFileClip('BothDetected_LiveVideo.mp4')
            clip.write_videofile("BothvideoLive.mp4")
            st_video = open('BothvideoLive.mp4','rb')
            video_bytes = st_video.read()
            st.video(video_bytes)
            st.write("Detected Video") 
            st.markdown(get_binary_file_downloader_html('BothvideoLive.mp4', 'Video'), unsafe_allow_html=True)
        except OSError:
            ''

if __name__ == '__main__':
		main()	