from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_EVEN
from brain_games.utils import get_rand_num


def is_even(number):
    return number % 2 == 0


def get_even_or_odd_num_and_answer():
    number = get_rand_num()
    answer = 'yes' if is_even(number) else 'no'
    return number, answer


def run_even_game():
    start_game(get_even_or_odd_num_and_answer, DESCRIPTION_EVEN)
