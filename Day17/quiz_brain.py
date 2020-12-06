class QuizBrain:
    def __init__(self,qlist):
        self.question_list = qlist
        self.question_number = 0
        self.score = 0

    def nextQuestion(self):
        self.question_number += 1
        question = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number}: {question.text} (True/False)? : ")
        self.checkAnswer(ans)

    def stillHasQuestion(self):
        return self.question_number < len(self.question_list)

    def checkAnswer(self,ans):
        if(ans.lower() == self.question_list[self.question_number].ans.lower()):
            print("You Got It Right!")
            self.score += 1
        else:
            print("You Got It Wrong!!!")

        print(f"The Correct Answer Was {self.question_list[self.question_number].ans}")
        print(f"Your Current Score is {self.score}/{self.question_number}")