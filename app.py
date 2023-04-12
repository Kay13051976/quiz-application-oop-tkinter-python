#import class and data from another file
from question import Question
from data import question_data
from controller import Controller
from ui import UserInterface

all_question=[]

#  compose a question 
for item in question_data:
    text=item["text"]
    answer=item["answer"]
    question=Question(text,answer)
    all_question.append(question)

#built controller
controller = Controller(all_question)
userInterface = UserInterface(controller)








