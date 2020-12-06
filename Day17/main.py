from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for quesiton in question_data:
    question_bank.append(
        Question(quesiton["text"],quesiton["answer"])
    )

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()
    print("\n\n")

print("You Have Completed The Quiz!!!!")
print(f"Your Final Score : {quiz.score}/quiz.question_number")