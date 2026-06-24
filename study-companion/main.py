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


def study_mode():
    topic = input("\nWhat topic are you studying? ")

    print("\nStudy Companion Plan")
    print("--------------------")
    print("Topic:", topic)
    print("1. Explain the topic in simple words")
    print("2. Show one example")
    print("3. Ask one practice question")
    print("4. Review what you got wrong")


def main():
    while True:
        print("\n=== AI Study Companion v3 ===")
        print("1. Study Mode")
        print("2. Python Quiz")
        print("3. Driver's Test Quiz")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            study_mode()
        elif choice == "2":
            python_quiz()
        elif choice == "3":
            drivers_test_quiz()
        elif choice == "4":
            print("Good job studying today.")
            break
        else:
            print("Invalid choice. Choose 1, 2, 3, or 4.")


main()
