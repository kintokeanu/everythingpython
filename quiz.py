#create a dictionary to store the question and answer
quiz = {
    "Question1": {
        "Question": " who coaches afc? ",
        "answer": "arteta"
    },
    "Question2": {
        "Question": " who coaches man u? ",
        "answer": "ten hag"
    },
    "Question3": {
        "Question": " who coaches man city? ",
        "answer": "pep"
    },
    "Question4": {
        "Question": " who coaches liverpool ",
        "answer": "klopp"
    },
    "Question5": {
        "Question": " who coaches spurs? ",
        "answer": "conte"
    },
}

#set default score
score = 0

#loop through the questions
for key, value in quiz.items():
    print(value['Question'])
    answer = input("Answer? ")
# lower() perevents a case error
    if answer.lower() == value['answer'].lower():
        print("correct")
        score = score + 1
        print("your score is: " + str(score))
        print("")
        print("")

    else:
        print("wrong")
        print("the answer is: " + value["answer"])
        print("Your score is: " +str(score))
        print("")
        print("")


print("You got " + str(score) + "out of 5 questions correctly")
print("Your percentage is " + str(int(score/5 * 100)))

