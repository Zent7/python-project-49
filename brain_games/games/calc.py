import random
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_CALC, MATH_SIGNS
from brain_games.utils import get_rand_num


def get_result_by_math_sign(num1, num2, math_sign):
    match math_sign:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError('Unsupported operator')


def get_math_expression_and_result():
    num1, num2 = get_rand_num(), get_rand_num()
    math_sign = random.choice(MATH_SIGNS)

    math_expression = f"{num1} {math_sign} {num2}"
    result = get_result_by_math_sign(num1, num2, math_sign)

    return math_expression, str(result)


def run_calc_game():
    start_game(get_math_expression_and_result, DESCRIPTION_CALC)