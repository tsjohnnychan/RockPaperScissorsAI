from random import randint

class Game_Engine():

    def __init__(self):
        self.moves = ['Rock','Paper','Scissors']
        self.computer_score = 0
        self.player_score = 0
        self.computer_plays = []
        self.player_plays = []

    def set_scores(self,who_won):
        if who_won == 'computer':
            self.computer_score += 1
        elif who_won == 'player':
            self.player_score += 1
        else:
            raise Exception('Unknow player name')

    def play_a_hand(self, player):

        #assign a random play to the computer
        computer = self.moves[randint(0,2)]
        self.computer_plays.append(computer)
        self.player_plays.append(player)
        
        # compare moves
        if player == computer:
            print('Tie!')
            return 'TIE'
        elif player == 'Rock':
            if computer == 'Paper':
                print('You lose...', computer, 'covers', player)
                return 'LOST'
            else:
                print('You win!', player, 'smashes', computer)
                return 'WON'
        elif player == 'Paper':
            if computer == 'Scissors':
                print('You lose...', computer, 'cut', player)
                return 'LOST'
            else:
                print('You win!', player, 'covers', computer)
                return 'WON'
        elif player == 'Scissors':
            if computer == 'Rock':
                print('You lose...', computer, 'smashes', player)
                return 'LOST'
            else:
                print('You win!', player, 'cut', computer)
                return 'WON'
        else:
            print('That iPs not a valid play. Check your spelling!')  
            return None      

    def play_to_win(self):
        while True:
            player = input('Rock, Paper, Scissors? ')
            result = self.play_a_hand(player)
            if result is None:
                break
            else:
                if result == 'WON':
                    self.set_scores('computer')
                    break
                elif result == 'LOST':
                    self.set_scores('player')
                    break

    def play_multiple_hands(self,tot_hand):
        hand = 1
        while hand <= tot_hand:
            player = input('Rock, Paper, Scissors? ')
            result = self.play_a_hand(player)
            if result == 'TIE':
                hand += 1
            elif result == 'WON':
                self.set_scores('player')
                hand += 1
            elif result == 'LOST':
                self.set_scores('computer')
                hand += 1
        print (
            'Final scores: computer -- {}, player -- {}'.format(
                self.computer_score, self.player_score
                )
            )

    def auto_play(self,tot_hand):
        # computer plays against computer
        hand = 1
        while hand <= tot_hand:
            player = self.moves[randint(0,2)]
            result = self.play_a_hand(player)
            if result == 'TIE':
                hand += 1
            elif result == 'WON':
                self.set_scores('player')
                hand += 1
            elif result == 'LOST':
                self.set_scores('computer')
                hand += 1
        print (
            'Final scores: computer -- {}, player -- {}'.format(
                self.computer_score, self.player_score
                )
            )

if __name__ == "__main__":
    ge = Game_Engine()
    ge.auto_play(10)
