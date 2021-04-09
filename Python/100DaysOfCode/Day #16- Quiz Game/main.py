from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

match = QuizBrain(question_bank)

while match.still_has_questions():
    match.next_question()


print("You've finished the quiz!")
print(f"Your final score was: {match.score}/{match.number}!")
