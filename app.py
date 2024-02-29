from flask import Flask, render_template
from ultralytics import YOLO

app = Flask(__name__)

model_path = 'yolov8s.pt'
image_path = 'static/5.jpg'
file_name = '5.jpg'

model = YOLO(model_path)
results = model(image_path, classes=[1, 2, 3, 5, 7])
result = results[0]

@app.route("/")
def helloWorld():
    return render_template('home.html',result=len(result.boxes))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)