from importlib import reload
from django.shortcuts import render
#from .models import PredResults
import pandas as pd
# Create your views here.

import joblib
reloadModel = joblib.load('./models/heart_model.pkl')

def index(request):
    temp={}
    context= {'temp':temp}
    return render(request, 'index.html',context)

def heart(request):
    print(request)
    if request.method == 'POST':
            
        temp={}
        temp['age'] = request.POST.get('age')
        temp['sex'] = request.POST.get('sex')
        temp['cp'] = request.POST.get('cp')
        temp['trestbps'] = request.POST.get('trestbps')
        temp['chol'] = request.POST.get('chol')
        temp['fbs'] = request.POST.get('fbs')
        temp['restecg'] = request.POST.get('restecg')
        temp['thalach'] = request.POST.get('thalach')
        temp['exang'] = request.POST.get('exang')
        temp['oldpeak'] = request.POST.get('oldpeak')
        temp['slope'] = request.POST.get('slope')
    testdata=pd.DataFrame({'x':temp}).transpose()
    val=reloadModel.predict(testdata)[0]
    if val == 1:
        scoreval = 'affected'
    else:
        scoreval = 'unaffected'

    context={'scoreval':scoreval,'temp':temp}
    return render(request,'index.html',context)

    
#temp={}
#temp['age']=1
#temp['sex']=2
#temp['cp']=3
#temp['trestbps']=4
#temp['chol']=5
#temp['fbs']=6
#temp['restecg']=1
#temp['thalach']=6
#temp['exang']=6
#temp['oldpeak']=6
#temp['slope']=6

    #df=pd.read_csv('heart_statlog_cleveland_hungary_final.csv')
  #  testdata= pd.DataFrame({'x':}).transpose()
#    scoreval = model.predict(testdata)[0]
 #   context= {'scoreval':scoreval}
    #ml_model = joblib.load(model_reg)
    #result = ml_model.predict([])
    #Heart_dis = result[0]
    #PredResults.objects.create(age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol, 
    #fbs=fbs, restecg=restecg, thalach=thalach, exang=exang, oldpeak=oldpeak,slope=slope, Heart_dis=Heart_dis)
    #data = {"dataset": PredResults.objects.all()}
    #return render(request, "index.html", data)