import os
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import pandas as pd
import gunicorn
scaler = StandardScaler()
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import category_encoders as ce
import zipfile
import os
app = Flask(__name__)
model = pickle.load(open('techncolabs_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        

        hist_user_behavior_is_shuffle = float(request.form['hist_user_behavior_is_shuffle'])
        hist_user_seek_behavior = float(request.form['hist_user_seek_behavior'])        
        time_of_day = request.form['time_of_day']   
        if(time_of_day=='dawn'):
            time_of_day="dawn"
        elif(time_of_day=='early_morning'):
            time_of_day="early_morning"
        elif(time_of_day=='morning'):
            time_of_day="morning"            
        elif(time_of_day=='mid_morning'):
            time_of_day="mid_morning"             
        elif(time_of_day=='noon'):
            time_of_day="noon"             
        elif(time_of_day=='afternoon'):
            time_of_day="afternoon"               
        elif(time_of_day=='evening'):
            time_of_day="evening"    
        else:
            time_of_day="night"  
            
        release_condition = request.form['release_condition']
        if(release_condition=='very_old'):
            release_condition="very_old"
        elif(release_condition=='old'):
            release_condition="old"
        elif(release_condition=='relatively_old'):
            release_condition="relatively_old"            
        elif(release_condition=='new'):
            release_condition="new"             
        elif(release_condition=='mordern'):
            release_condition="mordern"              
        else:
            release_condition="latest"        
        
        
        
        
        
        
        session_position = float(request.form['session_position'])
        session_length = float(request.form['session_length'])
        context_switch = float(request.form['session_length'])        
        no_pause_before_play = float(request.form['no_pause_before_play'])                
        hist_user_behavior_n_seekfwd = float(request.form['hist_user_behavior_n_seekfwd'])                
        hist_user_behavior_n_seekback = float(request.form['hist_user_behavior_n_seekback'])                
        premium = float(request.form['premium'])  
              
        context_type = request.form['context_type']   
        if(context_type=='user_collection'):
            context_type="user_collection"
        elif(context_type=='catalog'):
            context_type="catalog"
        elif(context_type=='editorial_playlist'):
            context_type="editorial_playlist"            
        elif(context_type=='radio'):
            context_type="radio"             
        elif(context_type=='personalized_playlist'):
            context_type="personalized_playlist"              
        else:
            context_type="charts"  



            
        hist_user_behavior_reason_start = request.form['hist_user_behavior_reason_start']
        if(hist_user_behavior_reason_start=='fwdbtn'):
            hist_user_behavior_reason_start="fwdbtn"
        elif(hist_user_behavior_reason_start=='trackdone'):
            hist_user_behavior_reason_start="trackdone"
        elif(hist_user_behavior_reason_start=='clickrow'):
            hist_user_behavior_reason_start="clickrow"            
        elif(hist_user_behavior_reason_start=='backbtn'):
            hist_user_behavior_reason_start="backbtn"             
        elif(hist_user_behavior_reason_start=='appload'):
            hist_user_behavior_reason_start="appload"             
        elif(hist_user_behavior_reason_start=='playbtn'):
            hist_user_behavior_reason_start="playbtn"               
        elif(hist_user_behavior_reason_start=='remote'):
            hist_user_behavior_reason_start="remote"  
        elif(hist_user_behavior_reason_start=='trackerror'):
            hist_user_behavior_reason_start="trackerror"  
        else:
            hist_user_behavior_reason_start="endplay" 



               
        hist_user_behavior_reason_end = request.form['hist_user_behavior_reason_end']  
        if(hist_user_behavior_reason_end=='fwdbtn'):
            hist_user_behavior_reason_end="fwdbtn"
        elif(hist_user_behavior_reason_end=='trackdone'):
            hist_user_behavior_reason_end="trackdone"
        elif(hist_user_behavior_reason_end=='clickrow'):
            hist_user_behavior_reason_end="clickrow"            
        elif(hist_user_behavior_reason_end=='backbtn'):
            hist_user_behavior_reason_end="backbtn"             
        elif(hist_user_behavior_reason_end=='logout'):
            hist_user_behavior_reason_end="logout"                           
        elif(hist_user_behavior_reason_end=='remote'):
            hist_user_behavior_reason_end="remote"  
        else:
            hist_user_behavior_reason_end="endplay"         
        
        
        
        
        
        
        
        
        
        
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
        mode = request.form['mode']
        if(mode=='major'):
            mode="major"
        else:
            mode="minor"




         
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

        prediction=model.predict([[hist_user_behavior_is_shuffle,hist_user_seek_behavior,time_of_day,release_condition,session_position,session_length,context_switch,no_pause_before_play,hist_user_behavior_n_seekfwd,hist_user_behavior_n_seekback,premium,context_type,hist_user_behavior_reason_start,hist_user_behavior_reason_end,duration,us_popularity_estimate,acousticness,beat_strength,bounciness,danceability,dyn_range_mean,energy,instrumentalness,flatness,liveness,loudness,mechanism,organism,speechiness,mode,tempo,valence,acoustic_vector_0,acoustic_vector_1,acoustic_vector_2,acoustic_vector_3,acoustic_vector_4,acoustic_vector_5, acoustic_vector_6,acoustic_vector_7]]) 
        p=model.predict(prediction)
         
        if p==0:
            return render_template('index.html',prediction_texts="Based on the given inputs, the song should not be skipped")
        else:
            return render_template('index.html',prediction_texts="Based on the given inputs, the song should be skipped")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
