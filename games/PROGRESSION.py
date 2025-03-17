import random

from engine import run_game


def generate_progression_question():

    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 6)

    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer


if __name__ == "__main__":
    run_game("Fid missing in the progression?", generate_progression_question)
