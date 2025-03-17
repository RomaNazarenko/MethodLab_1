import random

from engine import run_game


def NOD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def NOK(a, b):
    return abs(a * b) // NOD(a, b)


def generate_nok_question():

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)
    correct_answer = NOK(NOK(num1, num2), num3)
    question = f"{num1} {num2} {num3}"
    return question, correct_answer


if __name__ == "__main__":
    run_game("Find the nok.", generate_nok_question)

