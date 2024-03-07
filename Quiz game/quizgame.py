import questions as que


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer(A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer is", question["answer"], "\n")
    print(f"Your total score is {score}")



run_quiz(que.questions)
