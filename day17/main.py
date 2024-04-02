from question import Question
from data import question_data
from quiz import Quiz

question_bank = []

for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = Quiz(question_bank)

while quiz.still_has_questions():

    quiz.ask_question()