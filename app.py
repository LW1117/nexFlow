from flask import Flask, render_template
from detect import objectDetect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/detect")
def detect():
    results = objectDetect()
    return render_template('detect.html',result=len(results[0].boxes))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)