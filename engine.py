def run_game(game_rules, generate_question):

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_rules)

    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        try:
            user_answer = input("Your answer: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
        except ValueError:
            print(f"Invalid input! Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
