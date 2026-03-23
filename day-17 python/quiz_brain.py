from question_model import *
from main import *
import random
# question = Question()

class QuizBrain:
    def __init__(self,q_list):
        self.questions_number = 0
        self.question_list = q_list

    def next_question(self):

