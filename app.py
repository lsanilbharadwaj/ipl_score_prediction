# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:02:37 2021

@author: lsani
"""

from flask import Flask, request, render_template
import pickle

import numpy as np
app = Flask(__name__)

s='ipl_model.pkl'
model = pickle.load(open(s,'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('input.html')

@app.route("/predict",methods=['POST'])
def pred():
   tp=[]
   
   if request.method == 'POST':
       
      runs=int(request.form['runs'])
      wicket=int(request.form['wickets'])
      delivery=float(request.form['overs'])
      last_4overs_runs=int(request.form['runs_in_prev_4'])
      last_4overs_wickets = int(request.form['wickets_in_prev_4'])

      tp= tp + [delivery,runs, wicket, last_4overs_runs, last_4overs_wickets]
       
      if request.form['venue']=='Dr DY Patil Sports Academy, Navi Mumbai':
          tp=tp+[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Eden Gardens, Kolkata':
          tp=tp+[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Feroz Shah Kotla Stadium, Delhi':
          tp=tp+[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='M Chinnaswamy Stadium, Bangalore':
          tp=tp+[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='MA Chidambaram Stadium, Chepauk-Chennai':
          tp=tp+[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='MCA-Subrata Roy Sahara Stadium, Pune':
          tp=tp+[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Narendra Modi Stadium, Motera, Ahmedabad':
          tp=tp+[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Other':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]          
      elif request.form['venue']=='Punjab Cricket Association Stadium, Mohali':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
      elif request.form['venue']=='Rajiv Gandhi International Stadium, Uppal-Hyderabad':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
      elif request.form['venue']=='Sawai Mansingh Stadium, Jaipur':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
      elif request.form['venue']=='Wankhede Stadium, Mumbai':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
           
                  

      if request.form['batting-team']=='Chennai Super Kings':
         tp=tp+[1, 0, 0, 0, 0, 0, 0, 0]
         bat='Chennai Super Kings'
      elif request.form['batting-team']=='Delhi Capitals':
         tp = tp + [0, 1, 0, 0, 0, 0, 0, 0]
         bat='Delhi Capitals'
      elif request.form['batting-team']=='Kolkata Knight Riders':
         tp = tp + [0, 0, 1, 0, 0, 0, 0, 0]
         bat='Kolkata Knight Riders'
      elif request.form['batting-team']=='Mumbai Indians':
         tp = tp + [0, 0, 0, 1, 0, 0, 0, 0]
         bat='Mumbai Indians'
      elif request.form['batting-team']=='Punjab Kings':
         tp = tp + [0, 0, 0, 0, 1, 0, 0, 0]
         bat='Punjab Kings'
      elif request.form['batting-team']=='Rajasthan Royals':
         tp = tp + [0, 0, 0, 0, 0, 1, 0, 0]
         bat='Rajasthan Royals'
      elif request.form['batting-team']=='Royal Challengers Bangalore':
         tp = tp + [0, 0, 0, 0, 0, 0, 1, 0]
         bat='Royal Challengers Bangalore'
      elif request.form['batting-team']=='Sunrisers Hyderabad':
         tp = tp + [0, 0, 0, 0, 0, 0, 0, 1]
         bat='Sunrisers Hyderabad'

      if request.form['bowling-team']=='Chennai Super Kings':
         tp=tp+[1, 0, 0, 0, 0, 0, 0, 0]
         bowl='CSK'
      elif request.form['bowling-team']=='Delhi Capitals':
         tp = tp + [0, 1, 0, 0, 0, 0, 0, 0]
         bowl='DC'
      elif request.form['bowling-team']=='Kolkata Knight Riders':
         tp = tp + [0, 0, 1, 0, 0, 0, 0, 0]
         bowl='KKR'
      elif request.form['bowling-team']=='Mumbai Indians':
         tp = tp + [0, 0, 0, 1, 0, 0, 0, 0]
         bowl='MI'
      elif request.form['bowling-team']=='Punjab Kings':
         tp = tp + [0, 0, 0, 0, 1, 0, 0, 0]
         bowl='PBKS'
      elif request.form['bowling-team']=='Rajasthan Royals':
         tp = tp + [0, 0, 0, 0, 0, 1, 0, 0]
         bowl='RR'
      elif request.form['bowling-team']=='Royal Challengers Bangalore':
         tp = tp + [0, 0, 0, 0, 0, 0, 1, 0]
         bowl='RCB'
      elif request.form['bowling-team']=='Sunrisers Hyderabad':
         tp = tp + [0, 0, 0, 0, 0, 0, 0, 1]
         bowl='SRH'


      

      p=np.array([tp])
      print(p)

      score=(int(model.predict(p)[0]))
      lw=score-3
      up=score+3

      
      return render_template('input.html',score="{} will need to chase runs between {}-{} to win the match against {}".format(bowl,lw,up,bat))
      

if __name__ == '__main__':
   app.run(debug = True)