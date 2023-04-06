import sys
import cv2 
import imutils
from yolov5Det import YoloV5TRT

model = YoloV5TRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build/yolov5s.engine", conf=0.5)
cap = cv2.VideoCapture("videos/testvideo.mp4")
while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    detections = model.Inference(frame)
    # for obj in detections:
    #    print(obj['class'], obj['conf'], obj['box'])
    cv2.imshow("Output", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()