class RockPaperScissors():

    def __init__(self, ai_player):
        self.mapping = {
            'Rock': 'r', 'rock': 'r', 'r': 'r', 'R': 'r',
            'Paper': 'p', 'paper': 'p', 'p': 'p', 'P': 'p',
            'Scissors': 's', 'scissors': 's', 's': 's', 'S': 's'
        }
        self.ai_moves = []
        self.human_moves = []
        self.ai_player = ai_player


    def judge(self, move_1, move_2):
        ''' judge if move_1 win, lose, tie '''
        move_1 = self.mapping[move_1]
        move_2 = self.mapping[move_2]
        if move_1 == move_2:
            return 'TIE'
        elif move_1 == 'r':
            if move_2 == 'p':
                return 'LOSE'
            else:
                return 'WIN'
        elif move_1 == 'p':
            if move_2 == 's':
                return 'LOSE'
            else:
                return 'WIN'
        elif move_1 == 's':
            if move_2 == 'r':
                return 'LOSE'
            else:
                return 'WIN'
        else:
            print('That iPs not a valid play. Check your spelling!')  
            return None      

    def calc_scores(self,ai_moves=None,human_moves=None):
        if ai_moves is None:
            ai_moves = self.ai_moves
        if human_moves is None:
            human_moves = self.human_moves
        ai_score = 0 
        human_score = 0
        for ai_move, human_move in zip(ai_moves, human_moves):
            result = self.judge(ai_move, human_move)
            if result == 'WIN':
                ai_score += 1
            elif result == 'LOSE':
                human_score += 1
        return ai_score, human_score

    def render(self, ai_learns=False):
        while True:
            # ask for inputs
            ai_move = input('ai move = ')
            human_move = input('human move = ')
            self.ai_moves.append(ai_move)
            self.human_moves.append(human_move)
            # judge rules
            result = self.judge(ai_move, human_move)
            if result == 'TIE':
                print ('AI ties with Human')
            elif result == 'WIN':
                print ('AI won')
            elif result == 'LOSE':
                print ('Human won')
            # ai learns
            if ai_learns:
                pass

            if input('Continue? (yes/no)') == 'no':
                break
        ai_score, human_score = self.calc_scores()
        return ai_score, human_score
