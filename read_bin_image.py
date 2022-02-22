from PIL import Image
import io
import sys
import numpy as np
from skimage import transform

from tensorflow import keras
model2 = keras.models.load_model("mobile_net.h5")

def read_image(file_name):
    print(file_name)
    image_data = open(file_name, 'rb').read()
    image = Image.open(io.BytesIO(image_data))
    print(image.size)
    image.resize((160,160))
    image.show()


def load(filename):
    np_image = open(filename, 'rb').read()
    np_image=Image.open(io.BytesIO(np_image))
    np_image = np.array(np_image).astype('float32')
    np_image = transform.resize(np_image, (160, 160, 3))
    np_image = np.expand_dims(np_image, axis=0)
    print(np_image.shape)
    return np_image

def predict( image_address):
    test_image=Image.open(image_address)
    inp_org=np.array(test_image)
    image = load(image_address)
    cls=model2.predict(image)
    if np.round(cls[0])==0:
        lbl="Jewelry"
    elif np.round(cls[0])==1:
        lbl="Other"
    print(lbl)


if __name__ == '__main__':
    #print('test')
    #print(sys.argv[0])
    predict(sys.argv[1])
