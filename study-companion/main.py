def python_study():
    topic = input("What Python topic do you need help with? ")

    print("\nPython Study Mode")
    print("-----------------")
    print("Topic:", topic)
    print("1. Read your notes")
    print("2. Look at one example")
    print("3. Try one practice problem")
    print("4. Ask AI to quiz you")


def drivers_test_study():
    print("\nDriver's Test Mode")
    print("------------------")
    print("Study these areas:")
    print("- Road signs")
    print("- Right-of-way")
    print("- Parking rules")
    print("- Safe driving laws")


def quiz_mode():
    score = 0

    print("\nQuiz Mode")
    print("---------")

    answer = input("In Python, what keyword is used to create a function? ")

    if answer.lower() == "def":
        print("Correct!")
        score += 1
    else:
        print("Not quite. The correct answer is def.")

    print("Your score:", score, "/ 1")


def study_companion():
    print("=== AI Study Companion ===")
    print("1. Python Study")
    print("2. Driver's Test Study")
    print("3. Quiz Mode")

    choice = input("\nChoose an option: ")

    if choice == "1":
        python_study()
    elif choice == "2":
        drivers_test_study()
    elif choice == "3":
        quiz_mode()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


study_companion()
