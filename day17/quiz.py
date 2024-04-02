# Asking the questions
# Check the answers are correct
# Check if the user is at the end of the quiz

from data import question_data

class Quiz:

    def __init__(self, question_list):
        self.question_list = question_list
        self.number = 0
        self.score = 0


    def ask_question(self):
    
        answer = input(f"Q.{self.number + 1}. {self.question_list[self.number].text}. (True/False): ").title()  
        self.check_answer(answer, self.question_list[self.number].answer)      
        self.number += 1


    def still_has_questions(self):
        if self.number > (len(self.question_list) - 1):
            return False
        else:
            return True


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You've got it right!")
        else:
            self.score -= 0.25
            print("You've got it wrong.")
        print(f"Your Score: {self.score}/{self.number + 1}")
