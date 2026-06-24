def study_companion():
    print("=== AI Study Companion ===")
    print("1. Python Study")
    print("2. Driver's Test Study")
    print("3. Quiz Mode")

    choice = input("\nChoose an option: ")

    if choice == "1":
        topic = input("What Python topic do you need help with? ")
        print(f"\nStudy Topic: {topic}")
        print("Review examples and practice problems.")

    elif choice == "2":
        print("\nDriver's Test Mode")
        print("Study road signs, right-of-way, and parking rules.")

    elif choice == "3":
        print("\nQuiz Mode Coming Soon!")

    else:
        print("Invalid choice.")

study_companion()
