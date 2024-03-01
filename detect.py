from ultralytics import YOLO


model_path = 'yolov8s.pt'
image_path = 'static/5.jpg'
file_name = '5.jpg'

model = YOLO(model_path)

def objectDetect():
    results = model(image_path, classes=[1, 2, 3, 5, 7])
    return results