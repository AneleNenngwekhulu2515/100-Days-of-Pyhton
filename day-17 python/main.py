from data import question_data
from question_model import Question

question_bank = Question(question_data["text"], question_data["answer"])

print(question_bank)
