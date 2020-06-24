from tensorflow.keras.layers import LSTM,Dense,Input
from tensorflow.keras.models import Model,save_model,load_model
import numpy as np
import pickle
from random import randint

class RockPaperScissorsAI():

    def __init__(self,reset=False):
        self.mapping = {
            'Rock': -1, 'rock': -1, 'r': -1, 'R': -1,
            'Paper': 0, 'paper': 0, 'p': 0, 'P': 0,
            'Scissors': 1, 'scissors': 1, 's': 1, 'S': 1
        }
        self.lookback = 5 # depth to analyze the prevous moves 
        if reset == False:
            try:
                self.model = self._create_model()
                self.model.load_weights('saved_model/weights')
                self.memory = self._load_memory()
            except:
                self.model = None
                self.memory = []
        else:
            self.model = None
            self.memory = []

    def _trim_memory(self, depth=10):
        if len(self.memory) > depth:
            self.memory = self.memory[-depth:]

    def _memorize(self,moves):
        self.memory = self.memory + moves

    def _map_moves2nums(self, moves):
        ''' map moves (list)  to nums (list) '''
        return [self.mapping[x] for x in moves]

    def _map_nums2moves(self, nums):
        ''' map nums (list) to moves (list) '''
        moves = []
        for num in nums:
            if num < -0.5:
                moves.append('Rock')
            elif num >= -0.5 and num <= 0.5:
                moves.append('Paper')
            elif num > 0.5:
                moves.append('Scissors')
            else:
                raise Exception ('Unknown number for mapping')
        return moves

    def _load_memory(self):
        return pickle.load(open('saved_model/memory.pkl','rb'))

    def _save_memory(self):
        pickle.dump(self.memory, open('saved_model/memory.pkl','wb'))


    def _fit(self, trainX, trainY, epochs):
        self.model.fit(trainX, trainY, epochs=epochs)

    def _predict(self,X):
        return self.model.predict(X)


    def _create_model(self):
        inputs = Input(shape=(self.lookback,1))
        lstm = LSTM(20,activation='tanh')(inputs)
        outputs = Dense(1)(lstm)
        model = Model(inputs, outputs)
        model.compile(loss='mse', optimizer='adam')
        return model

    def create_training_set(self, seq):
        X = []
        Y = []
        for i in range(0,len(seq)):
            if i - self.lookback < 0:
                pass
            elif i > len(seq):
                break
            else:
                X.append(seq[i-self.lookback:i])
                Y.append([seq[i]])
        trainX, trainY = np.array(X), np.array(Y)
        trainX = np.reshape(trainX,(trainX.shape[0],self.lookback,1))
        trainY = np.reshape(trainY,(trainY.shape[0],1))
        return trainX, trainY


    def predict_move(self):
        X = self.memory[-self.lookback:]
        X = self._map_moves2nums(X)
        X = np.array(X).reshape(1,self.lookback,1)
        yhat = self._predict(X)
        num = yhat[-1,0]
        print(num)
        moves = self._map_nums2moves([num])
        return moves[0]

    def take_counter_move(self, move):
        num = self._map_moves2nums([move])[0]
        if num == -1:
            cmove = 'Paper'
        elif num == 0:
            cmove = 'Scissors'
        elif num == 1:
            cmove = 'Rock'
        return cmove

    def take_random_move(self):
        moves = ['Rock','Paper','Scissors']
        return moves[randint(0,2)]

    def play(self):
        predicted_move = self.predict_move()
        counter_move = self.take_counter_move(predicted_move)
        return counter_move
    
    def learn(self,new_moves):
        self._memorize(new_moves)
        self._trim_memory()
        seq = self._map_moves2nums(self.memory)
        trainX, trainY = self.create_training_set(seq)
        self._fit(trainX, trainY, 50)
        self.model.save_weights('saved_model/weights')
        self._save_memory()
        
if __name__ == "__main__":
    
    def save_dummy_model():
        rock = RockPaperScissorsAI()
        moves = ['r','r','p','s','r','r','p','s','r','r','p','s','r','r','p','s']
        rock._memorize(moves)
        rock._trim_memory()
        seq = rock._map_moves2nums(moves)
        trainX, trainY = rock.create_training_set(seq)
        rock.model = rock._create_model()
        rock._fit(trainX, trainY, 200)
        rock.model.save_weights('saved_model/weights')
        rock._save_memory()    
    
    k = RockPaperScissorsAI()
    counter_move = k.play()
    k.learn(['r','r'])
    
    
    