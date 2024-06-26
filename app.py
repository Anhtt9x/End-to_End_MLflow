from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnn_Classifier.utils.common import decode_Image
from cnn_Classifier.pipeline.prediction import PredictionPipeLine

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)

CORS(app)


class ClientApp:
    def __init__(self):
        self.file_name = "input_image.jpg"
        self.classifier = PredictionPipeLine(self.file_name)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    #os.system("dvc repro")
    return "Training successfully"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decode_Image(image,clApp.file_name)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ =="__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)