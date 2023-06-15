from flask import Flask, jsonify, request
from VideoDeepfake.predictions import predict_video_main
import json
import subprocess
import torch
import shutil
import os
import threading




app = Flask(__name__)


def jsonOutput():  # Son indekse erişerek alıyoruz
    with open('saved/ShallowCNN_lfcc_I/best_pred.json') as dosya:
        veri = json.load(dosya)
    output = veri['y_pred'][-1]
    return(output)  

def run_another_script(script_path, arguments):
    command = ['python', script_path] + arguments
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)  # Betiğin çıktısını ekrana yazdır


script_path = 'train.py'
arguments = ['--feature_classname', 'lfcc', '--model_classname', 'ShallowCNN','--device','cuda' '--restore' ,  '--eval_only']


@app.route("/")
def home():
    return "Hello World"

@app.route("/api/predict-video", methods=["POST"])
def video():
    output = predict_video_main.predict_algorithm()
    return output


@app.route("/api/predict-audio", methods=["POST"])
def audio():

    video_file = request.files['audio']
    video_path = 'C:/Users/DELL/Desktop/SON/AudioDeepFakeDetection-master/data/fake/ljspeech_melgan/audiosave.wav'  # Video dosyasını kaydedeceğiniz yol
    video_file.save(video_path)
   # shutil.move("file", "data/fake/ljspeech_melgan")
    run_another_script(script_path, arguments)
    
    output = jsonOutput()
    print (output)
    if output == 0:
        os.remove(video_path)
        return "FAKE"
    elif output == 1:
        os.remove(video_path)
        return "REAL"
    else:
        os.remove(video_path)
        return "Please try again"

        
        
    
if __name__ == '__main__':
     app.run()