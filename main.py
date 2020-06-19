from game_engine import Game_Engine
from game_ai import Game_AI
from keras.layers import LSTM,Dense,Input
from keras.models import Model
import numpy as np

def create_training_set(seq, lookback):
    X = []
    Y = []
    for i in range(0,len(seq)):
        if i - lookback < 0:
            pass
        elif i > len(seq):
            break
        else:
            X.append(seq[i-lookback:i])
            Y.append([seq[i]])
    return np.array(X), np.array(Y)

GE = Game_Engine()
GE.auto_play(100)

GAI = Game_AI()
playdata = GAI.map_to_nums(GE.player_plays)

trainX, trainY = create_training_set(playdata,3)
trainX = np.reshape(trainX,(trainX.shape[0],3,1))
trainY = np.reshape(trainY,(trainY.shape[0],1))

inputs = Input(shape=(trainX.shape[1],trainX.shape[2]))
lstm = LSTM(50,activation='relu')(inputs)
outputs = Dense(1)(lstm)
model = Model(inputs, outputs)
model.compile(loss='mse', optimizer='adam')
model.fit(trainX, trainY, epochs=300)



