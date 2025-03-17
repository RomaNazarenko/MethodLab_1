from games import NOK, PROGRESSION


def main():
    print("Choose a game:")
    print("1. Geometric Progression")
    print("2. NOK")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        PROGRESSION.run_game("Find missing in the progression?",
                             PROGRESSION.generate_progression_question)
    elif choice == "2":
        NOK.run_game("Find the NOK.", NOK.generate_nok_question)
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()