import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, render_template

app = Flask(__name__, template_folder = 'templates')


def set_svoistvos(svoistvo1, svoistvo2, svoistvo3, svoistvo4, svoistvo5, svoistvo6, svoistvo7, svoistvo8, svoistvo9,
                  svoistvo10, svoistvo11, svoistvo12):
    model = keras.models.load_model("model for app")
    prediction = model.predict(
        [svoistvo1, svoistvo2, svoistvo3, svoistvo4, svoistvo5, svoistvo6, svoistvo7, svoistvo8, svoistvo9, svoistvo10,
         svoistvo11, svoistvo12])

    return prediction[0][0]


@app.route('/', methods=['post', 'get'])
def app_calculation():
    svoistvo_lst = []
    message = ''
    if request.method == 'POST':

        for i in range(1, 13, 1):
            svoistvo = request.form.get(f'svoistvo{i}')
            #print(svoistvo)
            svoistvo_lst.append(float(svoistvo))

        message = set_svoistvos(*svoistvo_lst)

    #
    return render_template("index.html", message=message)


app.run()