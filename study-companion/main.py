def run_quiz(title, questions):
    score = 0
    missed_topics = []

    print("\n" + title)
    print("-" * len(title))

    for question in questions:
        print("\n" + question["question"])
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Not quite.")
            print("Correct answer:", question["answer"])
            print("Explanation:", question["explanation"])
            missed_topics.append(question["topic"])

    print("\nQuiz Complete")
    print("Score:", score, "/", len(questions))

    if missed_topics:
        print("\nWeak Areas:")
        for topic in missed_topics:
            print("-", topic)
    else:
        print("\nNo weak areas today. Great job!")


def agent_mode():
    topic = input("\nWhat are you confused about? ").lower()

    if "loop" in topic:
        print("\nLOOPS EXPLAINED")
        print("----------------")
        print("A loop repeats code multiple times.")

        print("\nExample:")
        print("for number in range(5):")
        print("    print(number)")

        print("\nThis prints:")
        print("0")
        print("1")
        print("2")
        print("3")
        print("4")

        answer = input("\nPractice: What keyword starts a for loop? ").strip().lower()

        if answer == "for":
            print("Correct!")
        else:
            print("Not quite. The answer is: for")

    elif "function" in topic:
        print("\nFUNCTIONS EXPLAINED")
        print("-------------------")
        print("A function is a reusable block of code.")

        print("\nExample:")
        print("def greet():")
        print("    print('Hello')")

        answer = input("\nPractice: What keyword creates a function? ").strip().lower()

        if answer == "def":
            print("Correct!")
        else:
            print("Not quite. The answer is: def")

    elif "variable" in topic:
        print("\nVARIABLES EXPLAINED")
        print("-------------------")
        print("A variable stores information you can use later.")

        print("\nExample:")
        print("name = 'Orlando'")
        print("print(name)")

        answer = input("\nPractice: What symbol assigns a value to a variable? ").strip()

        if answer == "=":
            print("Correct!")
        else:
            print("Not quite. The answer is: =")

    else:
        print("\nI don't know that topic yet.")
        print("Try typing: Python loops, functions, or variables.")


def study_mode():
    topic = input("\nWhat topic are you studying? ")

    print("\nStudy Companion Plan")
    print("--------------------")
    print("Topic:", topic)
    print("1. Explain the topic in simple words")
    print("2. Show one example")
    print("3. Ask one practice question")
    print("4. Review what you got wrong")


def python_quiz():
    questions = [
        {
            "question": "What keyword is used to create a function in Python?",
            "answer": "def",
            "topic": "Functions",
            "explanation": "In Python, functions are created using the def keyword."
        },
        {
            "question": "What symbol is used to start a comment in Python?",
            "answer": "#",
            "topic": "Comments",
            "explanation": "Python uses the # symbol for single-line comments."
        },
        {
            "question": "What data type is used for True or False values?",
            "answer": "boolean",
            "topic": "Data Types",
            "explanation": "A boolean stores either True or False."
        }
    ]

    run_quiz("Python Quiz", questions)


def drivers_test_quiz():
    questions = [
        {
            "question": "At a stop sign, what must you do?",
            "answer": "stop",
            "topic": "Traffic Signs",
            "explanation": "You must come to a complete stop at a stop sign."
        },
        {
            "question": "What color is a warning sign usually?",
            "answer": "yellow",
            "topic": "Road Signs",
            "explanation": "Warning signs are usually yellow and alert drivers to hazards."
        },
        {
            "question": "Should you text while driving? yes or no",
            "answer": "no",
            "topic": "Safe Driving",
            "explanation": "Texting while driving is dangerous and illegal in many places."
        }
    ]

    run_quiz("Driver's Test Quiz", questions)


def main():
    while True:
        print("\n=== AI Study Companion v5 ===")
        print("1. Agent Mode")
        print("2. Study Mode")
        print("3. Python Quiz")
        print("4. Driver's Test Quiz")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            agent_mode()
        elif choice == "2":
            study_mode()
        elif choice == "3":
            python_quiz()
        elif choice == "4":
            drivers_test_quiz()
        elif choice == "5":
            print("Good job studying today.")
            break
        else:
            print("Invalid choice. Choose 1, 2, 3, 4, or 5.")


main()
