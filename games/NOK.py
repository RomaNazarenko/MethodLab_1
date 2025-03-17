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
    run_game("Find the smallest common multiple of given numbers.", generate_nok_question)


# import random
# #НОД
# def NOD(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# #НОК
# def NOK(a, b):
#     return abs(a * b) // NOD(a, b)
# def main():
#     print("Welcome to the Brain Games!")
#     name = input("May I have your name? ")
#     print(f"Hello, {name}!")
#     print("Find the smallest common multiple of given numbers.")
#     for _ in range(3):
#         num1 = random.randint(1, 20)
#         num2 = random.randint(1, 20)
#         num3 = random.randint(1, 20)
#         print(f"Question: {num1} {num2} {num3}")
#         ans = int(input("Your answer: "))
#         correct_ans = NOK(NOK(num1, num2), num3)
#         if ans == correct_ans:
#             print("Correct!")
#         else:
#             print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
#             print(f"Let's try again, {name}!")
#             break
#     else:
#         print(f"Congratulations, {name}!")
# if __name__ == "__main__":
#     main()