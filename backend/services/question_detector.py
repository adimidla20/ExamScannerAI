import re

def detect_questions(text):

    lines = text.split('\n')

    questions = []

    current_question = ""

    for line in lines:

        line = line.strip()

        if re.match(r'^\d+\.', line):

            if current_question:
                questions.append(current_question.strip())

            current_question = line

        else:
            if current_question:
                current_question += " " + line

    if current_question:
        questions.append(current_question.strip())

    return questions