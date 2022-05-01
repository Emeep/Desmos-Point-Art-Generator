import cv2
import numpy as np
import os
from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def home():
    return render_template("index.html")

path = 'link to folder with pics'

lr = np.array([0, 0, 0])
ur = np.array([250, 250, 250])

allcoords = []

for f in os.listdir(path):
    img = cv2.imread(path + '\\' + f)
    img = cv2.resize(img, (28, 20), interpolation = cv2.INTER_AREA)
    img = cv2.inRange(img, lr, ur)
    img = cv2.flip(img, 0)

    n_x = 0
    n_y = 0

    carr = []

    for x in img:
        n_y = 0
        for y in x:
            if y == 255:
                coords = '(' + str(n_y) + ', ' + str(n_x) + ')'
                carr.append(coords)
            n_y += 1
        n_x += 1

    allcoords.append(carr)

    print('frame = ' + f)

print(allcoords)

@app.route('/')
def index():
    return json.dumps(allcoords)

app.run()
