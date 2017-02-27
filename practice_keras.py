# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:18:16 2017

@author: aslado
"""

from keras.models import Sequential
from keras.layers import Dense
import numpy

# fix random seed for reproductibility
seed = 7
numpy.random.seed(seed)

# load pima indian dataset
dataset = numpy.loadtxt('pima-indians-diabetes.csv',delimiter=',')

# checking data
#print(dataset) # view of dataset
#print(len(dataset)) # lenght of dataset 
#print(dataset.shape) # shape (rows, columns)

# split into input X and output Y variables
X = dataset[:,0:8]
Y = dataset[:,8]

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8,init='uniform',activation='relu'))
model.add(Dense(1,init='uniform',activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X,Y, nb_epoch=150, batch_size=10)

# evaluate the model
scores = model.evaluate(X,Y)
print('%s:%.2f%%' % (model.metrics_names[1], scores[1]*100))