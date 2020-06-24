from game_ai import Game_AI

GAI = Game_AI(reset=True)

plays = ['r','p','p','s','s','r','p','s','r','p','s','r','p','s']

seq = GAI.map_plays2nums(plays)

trainX, trainY = GAI.create_training_set(seq,3)

GAI.create_model(trainX)
GAI.learn(trainX,trainY,300)
GAI.memorize(plays)

move = GAI.predict_move('r')

cmove = GAI.couter_move(move)