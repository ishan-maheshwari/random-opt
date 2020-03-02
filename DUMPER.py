# -*- coding: utf-8 -*-

import numpy as np

from sklearn import preprocessing
import sklearn.model_selection as ms
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

spam = pd.read_hdf('datasets.hdf','spam')     
spamX = spam.drop('Y',1).copy().values
spamY = spam['Y'].copy().values
le = preprocessing.LabelEncoder()
spamY = le.fit_transform(spamY)

# split dataset into training (70%) and test (30%) sets    
spam_trgX, spam_tstX, spam_trgY, spam_tstY = ms.train_test_split(spamX, spamY, test_size=0.3, random_state=0,stratify=spamY)   
spam_trgY = np.atleast_2d(spam_trgY).T
spam_tstY = np.atleast_2d(spam_tstY).T

spam_trgX, spam_valX, spam_trgY, spam_valY = ms.train_test_split(spam_trgX, spam_trgY, test_size=0.2, random_state=1,stratify=spam_trgY)  

lb = preprocessing.LabelBinarizer()
spam_trgY = lb.fit_transform(spam_trgY)
spam_tstY = lb.fit_transform(spam_tstY)
spam_valY = lb.fit_transform(spam_valY)



tst = pd.DataFrame(np.hstack((spam_tstX,spam_tstY)))
trg = pd.DataFrame(np.hstack((spam_trgX,spam_trgY)))
val = pd.DataFrame(np.hstack((spam_valX,spam_valY)))
tst.to_csv('spam_test.csv',index=False,header=False)
trg.to_csv('spam_trg.csv',index=False,header=False)
val.to_csv('spam_val.csv',index=False,header=False)