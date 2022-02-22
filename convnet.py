from PIL import Image
import numpy as np
from skimage import transform
import matplotlib.pyplot as plt


from tensorflow import keras
model2 = keras.models.load_model("Conve_v2.h5")

def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')
    np_image = transform.resize(np_image, (32, 32, 3))/255
    np_image = np.expand_dims(np_image, axis=0)
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
    plt.imshow(inp_org)
    plt.title(lbl)
    print(lbl)
    plt.show()


if __name__ == "__main__":
    import sys
    try:
        print(sys.argv[1])
        predict(sys.argv[1]) 
    except:
        print("The input format is violated")
