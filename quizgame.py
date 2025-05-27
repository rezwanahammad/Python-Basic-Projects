questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Leo Tolstoy"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Hippo"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    }
]


def quiz_game(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])  # Fixed this line
        for option in question["options"]:
            print(option)
        answer = input("What's your answer? (A, B, C, D): ").strip().upper()
        if answer == question["answer"]:
            print("Correct answer champ..!!")
            score += 1
        else:
            print(
                f"Wrong answer boiii.. The correct answer was {question['answer']}.")
    print(f"\nYour final score is: {score}/{len(questions)}")


quiz_game(questions)
