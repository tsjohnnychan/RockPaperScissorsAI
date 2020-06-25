import streamlit as st
from env import RockPaperScissors
from rps_ai import RockPaperScissorsAI
import logging

def main():

    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        ["Start Game", "Show Source Code"]
    )

    if app_mode == "Start Game":
        # # init game environment
        # envi = init_game_env()

        # set title 
        title_ui('Rock Paper Scissors with AI')

        # set sidebar ui elements
        rock, paper, scissors = game_sidebar_ui()

        # play game
        if rock:
            play(envi,human_move='Rock')
        elif paper:
            play(envi,human_move='Paper')
        elif scissors:
            play(envi,human_move='Scissors')

        logging.info('memeory: {}'.format(envi.ai_player.memory))

    elif app_mode == "Show Source Code":
        st.code(get_file_content_as_string("app.py"))

def game_sidebar_ui():
    rock = st.sidebar.button('Rock')
    paper = st.sidebar.button('Paper')
    scissors = st.sidebar.button('Scissors')
    return rock, paper, scissors

def title_ui(title):
    st.title(title)
    st.text('')
    st.text('')
    st.text('')
    st.text('')


def result_ui(human_move, ai_move):
    # st.image('images/Human_{}.png'.format(human_move), width=300)
    # st.image('images/AI_{}.png'.format(ai_move), width=300)

    st.image(
        [
            'images/Human_{}.png'.format(human_move),
            'images/AI_{}.png'.format(ai_move)
        ],
        width = 300
    )

def get_file_content_as_string(path):
    response = open(path)
    return response.read()

def init_game_env():
    logging.info('init env...')
    ai_player = RockPaperScissorsAI(reset=False)
    game_env = RockPaperScissors(ai_player)
    return game_env

def play(envi,human_move):
    ai_move = envi.ai_player.play()
    envi.ai_moves.append(ai_move)
    envi.human_moves.append(human_move)
    result = envi.judge(ai_move, human_move)
    # if result == 'TIE':
    #     st.write ('{} vs {}, ties'.format(human_move, ai_move))
    # elif result == 'WIN':
    #     st.write ('{} vs {}, AI won'.format(human_move, ai_move))
    # elif result == 'LOSE':
    #     st.write ('{} vs {}, Human won'.format(human_move, ai_move))
    result_ui(human_move,ai_move)
    envi.ai_player.learn([human_move])
    logging.info('human_moves: '.format(envi.human_moves))
    logging.info('ai_moves: '.format(envi.ai_moves))




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    envi = init_game_env()
    main()