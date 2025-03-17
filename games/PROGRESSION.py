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
    run_game("What number is missing in the progression?", generate_progression_question)

# import random
#
#
# def generate_progression():
#     length = random.randint(5, 10)
#     start = random.randint(1, 10)
#     ratio = random.randint(2, 6)
#
#     progression = [start * (ratio ** i) for i in range(length)]
#     hidden_index = random.randint(0, length - 1)
#     correct_answer = progression[hidden_index]
#     progression[hidden_index] = '..'
#
#     return progression, correct_answer
#
#
# def main():
#     print("Welcome to the Brain Games!")
#     name = input("May I have your name? ")
#     print(f"Hello, {name}!")
#     print("What number is missing in the progression?")
#
#     for _ in range(3):
#         progression, correct_answer = generate_progression()
#         print("Question:", " ".join(map(str, progression)))
#
#         try:
#             user_answer = int(input("Your answer: "))
#         except ValueError:
#             print(f"Invalid input! Let's try again, {name}!")
#             break
#
#         if user_answer == correct_answer:
#             print("Correct!")
#         else:
#             print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
#             print(f"Let's try again, {name}!")
#             break
#     else:
#         print(f"Congratulations, {name}!")
#
#
# if __name__ == "__main__":
#     main()
