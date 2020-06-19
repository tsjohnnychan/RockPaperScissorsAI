from game_engine import Game_Engine
from keras.layers import LSTM, Dense, TimeDistributed, Input, RepeatVector, concatenate, BatchNormalization, Bidirectional, Dropout
from keras.models import Model
import numpy as np

seq = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,2,1,2,2,1,2,2,1,2,2]
X = []
Y = []
for i in range(0,len(seq)):
    step = 3
    if i+step == len(seq):
        break
    else:
        X.append(seq[i:i+step])
        Y.append([seq[i+step]])
print (X)
print (Y)

inputs = Input(shape=(3,1))
lstm = LSTM(50,activation='relu')(inputs)
outputs = Dense(1)(lstm)
model = Model(inputs, outputs)
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

trainX = np.array(X)
trainY = np.array(Y)

trainX = np.reshape(trainX,(trainX.shape[0],3,1))
trainY = np.reshape(trainY,(trainY.shape[0],1))
model.fit(trainX,trainY,epochs=300)

testX = np.array([1,2,2])
testX = testX.reshape((1,3,1))

yhat = model.predict(testX)
