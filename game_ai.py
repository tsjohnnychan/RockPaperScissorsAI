class Game_AI():

    def __init__(self,reset=False):
        self.mapping = {
            'Rock': -1,
            'Paper': 0,
            'Scissors': 1
        }
    
    def map_to_nums(self, plays):
        # map plays (list)  to nums (list)
        return [self.mapping[x] for x in plays]



