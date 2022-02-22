#Programmers: Nima Farnoodian and Atefeh Bahrami

'''Model is trained using Transfer Learning method. 
A moblie-net convolutional network that was already trained on 
Imagenet dataset with 14 million images is re-trained based on our new dataset that includes jewelry photos and negative photos. 
The accuracy on the test dataset is 98.12 percent. Only a few samples that mostly include hands were predicted wrongly. 
For more detail, please refere to Transfer Learning-MobileNet.ipynb notebook.'''


'''
NodeJs-Request example:

var request = require('request');
var options = {
  'method': 'POST',
  'url': 'http://ip:port/predict',
  'headers': {
    'Content-Type': 'application/octet-stream'
  },
  body: "<file contents here>"

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

'''

from PIL import Image
from flask import Flask,request, jsonify
ai_api = Flask(__name__)
import io
import numpy as np
from skimage import transform
import json
from tensorflow import keras

# Loeading the mobile_net model
mobile_net = keras.models.load_model("./model/mobile_net.h5")

def load(file):
    np_image=Image.open(io.BytesIO(file))
    np_image = np.array(np_image).astype('float32')
    np_image = transform.resize(np_image, (160, 160, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


def predict_mobile_net( file):
    image = load(file)
    cls=mobile_net.predict(image)
    if np.round(cls[0])==0:
        lbl="jewelry"
    elif np.round(cls[0])==1:
        lbl="other"
    print(lbl)
    return lbl

@ai_api.route('/')
def hello_world():
    return 'This is a jewelry classifier API for the group project at UCLouvain. To predict the label of the image please use /predict post command'

@ai_api.route('/predict', methods=["POST"])
def predict():
    bin_image = request.data
    lbl=predict_mobile_net(bin_image)
    #dictToReturn = {'label':lbl}
    #return jsonify(dictToReturn)
    return lbl



if __name__ == '__main__':

    # Opening JSON config file
    f = open('config.json')
    
    # returns JSON object as a dictionary
    config = json.load(f)
    print(config)
    host=config["host"]
    port=int(config["port_number"])
    f.close()

    ai_api.run(debug = True,host=host,port=port)
