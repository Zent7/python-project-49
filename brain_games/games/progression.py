import random
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_PROGRESSION
from brain_games.utils import get_rand_num
from brain_games.consts import PROGRESSION_LENGHT


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def hide_progression_value(progression, index):
    hidden_value = progression[index]
    progression[index] = '..'
    return progression, str(hidden_value)


def get_question_and_result():
    start, step = get_rand_num(), get_rand_num()

    progression = generate_progression(start, step, PROGRESSION_LENGHT)

    hidden_index = random.randint(0, len(progression) - 1)
    progression_with_hidden_value, result = (
        hide_progression_value(progression, hidden_index))

    question = ' '.join(str(i) for i in progression_with_hidden_value)
    return question, result


def run_progression_game():
    start_game(get_question_and_result, DESCRIPTION_PROGRESSION)
