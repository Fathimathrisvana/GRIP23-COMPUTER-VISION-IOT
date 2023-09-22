# GRIP23-COMPUTER-VISION-IOT-Task-1

1.Loading the Model and Configuration:

The process begins by loading a pre-trained object detection model, in this case, a MobileNet-based model.
Additionally, a configuration file (ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt) is provided to define the model's architecture and class labels.
Class labels, which specify the names of object classes that the model can detect, are loaded from a file (coco.names).
2.Setting Model Input Parameters:

Parameters related to the input image processing are configured.
The model's input size is set to 320x320 pixels.
Input scaling is specified as 1.0/127.5, which scales pixel values to the range [-1, 1].
The input mean values are set to (127.5, 127.5, 127.5), which corresponds to MobileNet's normalization.
Color channel swapping is enabled with model.setInputSwapRB(True).
3.Loading and Preparing an Image for Inference:

An image (street.jpg) is read using OpenCV (cv2) for inference.
The image is displayed for visualization using Matplotlib (plt).
4.Object Detection and Confidence Scoring (Image):

The loaded image is passed through the object detection model.
The model.detect() function returns three arrays:
ClassIndex: Predicted class indices for detected objects.
confidence: Confidence scores for each detection.
bbox: Bounding box coordinates for each detection.
Confidence scores represent the model's certainty in detecting objects.
5.Annotating Detected Objects (Image):

Detected objects are annotated on the image:
Bounding boxes are drawn around detected objects.
Class labels are added to the annotated boxes.
Confidence scores (in percentage form) are displayed.
6.Displaying the Annotated Image (Image):

The annotated image is displayed using Matplotlib.
Detected objects are visually highlighted on the image.
7.Video Object Detection (Optional):

An optional section demonstrates video object detection.
The code captures frames from a video (Pexels Videos 2880.mp4) or a camera (if the video cannot be opened).
For each frame, object detection and annotation are performed similarly to the image case.
8.Adjusting Confidence Threshold:

The confidence threshold (0.55 in the code) can be adjusted.
Objects with confidence scores above this threshold are considered valid detections.
By changing the threshold, you can control the trade-off between detection sensitivity and precision.
9.Displaying Video Stream with Annotations (Optional):

For video object detection, frames with annotations are displayed in real-time.
Pressing 'q' in the video window exits the application.
Releasing Resources:

After processing, video capture resources are released (cap.release()).
OpenCV windows are destroyed (cv2.destroyAllwindows()).


