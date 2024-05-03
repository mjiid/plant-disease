from flask import render_template, request, url_for, jsonify,redirect
from Green import app
from Green.constants import *
from random import shuffle,sample
import os
from .disease_detector import *

@app.route('/home')
@app.route('/')
def home():
    shuffle(TEAM_MEMBERS)
    return render_template('home.html',TEAM_MEMBERS=TEAM_MEMBERS)

@app.route('/get-started/<plant>')
def get_started(plant=''):
    if plant in PLANTS:
        global plant_name
        plant_name = plant
        return render_template('get_started.html')
    else : 
        return 'Invalid plant name'

@app.route('/chosing-plant',methods=['GET','POST'])
def chosing_plant():
    return render_template('choose_plant.html',PLANTS_IMGS=PLANTS_IMGS)

@app.route('/give-disease-name',methods=['POST'])
def give_disease_name():
    if request.method =='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        job=request.form.get('job')
        plant_img=request.files.get('plant-img')

        if plant_img and ('plant_name' in globals()):
            img_path=r'Green/static/img/user_plant/img.png'
            if os.path.exists(img_path):
                os.remove(img_path)
            plant_img.save(img_path)
            response=test_model(plant_name)
            disease_description= get_data_for_disease(response)

            disease_data={
                'name': response.replace('__',' ').replace('_',' '),
                'gallery_dir': response,
                'description': disease_description,
                'input_img': 'img/user_plant/img.png' 
            }

            _DOCTORS=sample(DOCTORS,k=4)
            return render_template('output.html',DOCTORS=_DOCTORS,disease_data=disease_data)
        
        return '.'

    
        





