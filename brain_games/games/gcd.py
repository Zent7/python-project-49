import math
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_GCD
from brain_games.utils import get_rand_num


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def get_nums_pair_and_gcd():
    num1, num2 = get_rand_num(), get_rand_num()
    nums_pair = f"{num1} {num2}"
    gcd = get_gcd(num1, num2)
    return nums_pair, str(gcd)


def run_gcd_game():
    start_game(get_nums_pair_and_gcd, DESCRIPTION_GCD)
