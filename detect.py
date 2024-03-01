import cv2
from ultralytics import YOLO


model_path = 'yolov8s.pt'
image_path = 'static/5.jpg'
file_name = '5.jpg'

model = YOLO(model_path)

def objectDetect(img):
    results = model(img, classes=[1, 2, 3, 5, 7])
    img_rgb = 0

    for i, r in enumerate(results):
    # Plot results image
        im_rgb = r.plot()  # BGR-order numpy array

    # Show results to screen (in supported environments)
    img_rgb = r.save()
    
    return results, img_rgb