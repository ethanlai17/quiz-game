from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    answer = question["correct_answer"]
    new_q = Question(question_text, answer)
    question_bank.append(new_q)

quiz_engine = QuizBrain(question_bank)

while quiz_engine.still_has_questions():
    quiz_engine.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz_engine.score}/{quiz_engine.question_number}")
