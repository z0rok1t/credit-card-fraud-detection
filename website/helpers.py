from django.db import models
import pandas as pd
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib



def predicting(file_data):
    preprocessed_data = pd.read_csv(file_data)
    X=preprocessed_data.drop(['Class'], axis=1)
    model = joblib.load('trained_model.pkl')
    predictions=model.predict(X)
    return predictions



def train_model(train_data):
    data=pd.read_csv(train_data)
    X=data.drop(['Class'], axis=1)
    Y=data['Class']
    xtrain,xtest=train_test_split(X, test_size=0.30, random_state=100)
    ytrain,ytest=train_test_split(Y, test_size=0.30, random_state=100)
    logit_model = LogisticRegression(max_iter=1000,penalty='l2')
    log=logit_model.fit(xtrain,ytrain)
    joblib.dump(log, 'trained_model.pkl')
