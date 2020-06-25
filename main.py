from env import RockPaperScissors
from rps_ai import RockPaperScissorsAI

ai = RockPaperScissorsAI(reset=True)

game = RockPaperScissors(ai_player=ai)

game.render(ai_learns=True)



