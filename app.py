from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('rf.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        

        hist_user_behavior_is_shuffle = float(request.form['hist_user_behavior_is_shuffle'])
        hist_user_seek_behavior = float(request.form['hist_user_seek_behavior'])        
        session_position = float(request.form['session_position'])
        session_length = float(request.form['session_length'])
        context_switch = float(request.form['session_length'])        
        no_pause_before_play = float(request.form['no_pause_before_play'])                
        hist_user_behavior_n_seekfwd = float(request.form['hist_user_behavior_n_seekfwd'])                
        hist_user_behavior_n_seekback = float(request.form['hist_user_behavior_n_seekback'])                
        premium = float(request.form['premium'])  
        
        duration = float(request.form['duration'])       
        us_popularity_estimate = float(request.form['us_popularity_estimate'])       
        acousticness = float(request.form['acousticness'])       
        beat_strength = float(request.form['beat_strength'])       
        bounciness = float(request.form['bounciness'])         
        danceability = float(request.form['danceability'])         
        dyn_range_mean = float(request.form['dyn_range_mean'])         
        energy = float(request.form['energy'])         
        instrumentalness = float(request.form['instrumentalness'])         
        flatness = float(request.form['flatness'])         
        liveness = float(request.form['liveness'])         
        loudness = float(request.form['loudness'])         
        mechanism = float(request.form['mechanism'])         
        organism = float(request.form['organism'])         
        speechiness = float(request.form['speechiness'])         
        tempo = float(request.form['tempo']) 
        valence = float(request.form['valence']) 
        acoustic_vector_0 = float(request.form['acoustic_vector_0']) 
        acoustic_vector_1 = float(request.form['acoustic_vector_1']) 
        acoustic_vector_2 = float(request.form['acoustic_vector_2']) 
        acoustic_vector_3 = float(request.form['acoustic_vector_3']) 
        acoustic_vector_4 = float(request.form['acoustic_vector_4'])    
        acoustic_vector_5 = float(request.form['acoustic_vector_5']) 
        acoustic_vector_6 = float(request.form['acoustic_vector_6']) 
        acoustic_vector_7 = float(request.form['acoustic_vector_7']) 

        prediction=model.predict([[hist_user_behavior_is_shuffle,hist_user_seek_behavior,session_position,session_length,no_pause_before_play,hist_user_behavior_n_seekfwd,hist_user_behavior_n_seekback,premium,context_type,duration,us_popularity_estimate,acousticness,beat_strength,bounciness,danceability,dyn_range_mean,energy,instrumentalness,flatness,liveness,loudness,mechanism,organism,speechiness,tempo,valence,acoustic_vector_0,acoustic_vector_1,acoustic_vector_2,acoustic_vector_3,acoustic_vector_4,acoustic_vector_5, acoustic_vector_6,acoustic_vector_7]]) 
        p=round(prediction[0],0)
         
        if p==0:
            return render_template('index.html',prediction_texts="Based on the given inputs, the song should not be skipped")
        else:
            return render_template('index.html',prediction_texts="Based on the given inputs, the song should be skipped")
    else:
        return render_template('index.html',prediction_texts="Input error")

if __name__=="__main__":
    app.run(debug=True)
