from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    item_text = item["text"]
    item_answer = item["answer"]
    new_q = Question(text=item_text, answer=item_answer)
    question_bank.append(new_q)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("The quiz is completed")
print(f"Your final score: {new_quiz.score}/{new_quiz.question_number}") # ou len(question_bank)