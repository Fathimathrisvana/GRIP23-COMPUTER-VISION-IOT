import cv2
import matplotlib.pyplot as plt
classNames = []
classFile = r"C:\Users\fathi\Documents\internship\coco.names"
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
configPath = r"C:\Users\fathi\Documents\internship\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = r"C:\Users\fathi\Downloads\frozen_inference_graph.pb"
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
img = cv2.imread(r"C:\Users\fathi\Documents\internship\street.jpg")
cv2.imshow("output",img)
classIds, confs, bbox = net.detect(img, confThreshold=0.5)
if len(classIds) != 0:
   for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
     cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
     cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
     cv2.putText(img, str(round(confidence * 100, 2))+"%", (box[0] + 161, box[1] + 30),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Output", img)
cv2.waitKey(0)
