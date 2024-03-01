from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from detect import objectDetect

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')

app.config['UPLOAD'] = upload_folder

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/detect", methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        try:
            os.remove(img[:7]+'results_'+img[15:])
        except:
            pass
        results, op_img = objectDetect(img)
        os.rename(op_img,'static/'+op_img)
        return render_template('detect.html',result=len(results[0].boxes), img=img, op_img=op_img)
    return render_template('detect.html',result=0,img=0,op_img=0)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)