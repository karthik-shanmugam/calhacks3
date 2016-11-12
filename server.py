from __future__ import print_function
import base64
import json
from imgurpython import ImgurClient
import threading
import random
from random import gauss
import os
from rapid import classify_image


imgur_client = "0f8ebdce6b83981"
imgur_secret = "f5b5ca46e0ea44e94b5cc3f6e9ebe4dc4a8aa254"
client = ImgurClient(imgur_client, imgur_secret)

from flask import Flask, request, send_from_directory
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return send_from_directory('face-demo', 'index.html')

@app.route('/<string:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory('face-demo', path)

@app.route('/emojis/<string:path>', methods=['GET'])
def static_proxy2(path):
    return send_from_directory('face-demo/emojis', path)


counter = 0
counter_lock = threading.Lock()

@app.route('/image', methods=['POST'])
def upload_image():
    #print(request.form['image'])
    global counter
    with counter_lock:
        filename = "images/image%d.jpeg" % counter
        counter += 1
    with open(filename, "wb") as fh:
        fh.write(base64.decodestring(bytes(request.form['image'][23:], 'utf-8')))
    link = upload_to_imgur(filename)
    os.remove(filename)
    emotion = classify_image(link)[0]
    return emotion


def upload_to_imgur(path):
    link = client.upload_from_path(path)['link']
    with open("links.txt", "a") as myfile:
        myfile.write("%s\n" % link)
    return link

# def classify_image(link):

#     # vec = [gauss(0, 1) for i in range(8)]
#     # mag = sum(x**2 for x in vec) ** .5
#     # vector = {emotion: score for emotion, score in zip(("anger","contempt","disgust","fear","happiness","neutral","sadness","surprise"), [x/mag for x in vec])}
#     return random.choice(["anger","contempt","disgust","fear","happiness","neutral","sadness","surprise"])
#     #return vector

# if __name__ == "__main__":
#     app.run(debug=True)