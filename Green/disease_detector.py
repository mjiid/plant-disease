from tensorflow import keras
import cv2
import numpy as np
import json
img_path=r'Green/static/img/user_plant/img.png'

def test_model(plant):
    model_path="Green/static/models/model_"+plant
    model=keras.models.load_model(model_path)

    with open(model_path+"/labels.json",'r') as f:
        data= json.load(f)
        keys_to_labels=data['keys_to_labels']
        print(f'{keys_to_labels=}')

    input_image = cv2.imread(img_path)

    input_image_resize = cv2.resize(input_image, (224,224))
    input_image_scaled = input_image_resize/255
    image_reshaped = np.reshape(input_image_scaled, [1,224,224,3])
    input_prediction = model.predict(image_reshaped)
 
    input_pred_label = str(np.argmax(input_prediction))
    return keys_to_labels.get(input_pred_label)

def get_data_for_disease(disease_name):
    with open(r'Green/static/diseases/data.json','r') as data:
        data=json.load(data)
    return data.get(disease_name)

    