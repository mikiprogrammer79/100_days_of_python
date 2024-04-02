from question import Question
from data import question_data, question_data2
from quiz import Quiz

question_bank = []

prompt = input("What quiz number do you want to do? Type 'A' or 'B':  ").lower()

if prompt == "a":

    for i in range(0, len(question_data)):
        question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

elif prompt == "b":

    for i in range(0, len(question_data2["results"])):
        question_bank.append(Question(question_data2["results"][i]["question"], question_data2["results"][i]["correct_answer"]))


quiz = Quiz(question_bank)

while quiz.still_has_questions():

    quiz.ask_question()



