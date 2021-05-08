#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QRadioButton, QApplication, QGroupBox

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
my_win = QWidget()
cur_question = -1
def next_question():
    my_win.total += 1
    print('Всего:', my_win.total)
    cur_question = randint(0, len(questions_list) - 1)
    g = questions_list[cur_question]
    ask(g)
    
def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    answer1.setText(q.right_answer)
    show_question()

def show_result():
    RadioGroupBox.hide()
    button.setText('Следующий вопрос')
    AnswerGroupBox.show()

def show_question():
    Radio1GroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    Radio1GroupBox.setExclusive(True)
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button.setText('Ответить')

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()

def show_correct(res):
    right_answer.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        my_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    rate = my_win.score / my_win.total * 100
    print('Правильно:', my_win.score)
    print('Рейтинг:', rate)

layout_main = QVBoxLayout()
my_win.setWindowTitle('Вопрос')
lb_question = QLabel('Вопрос')

questions_list = []
q1 = Question('1586 / 4', '396,5', '456', '563,5', '443,5')
q2 = Question('В саду росло 8 яблонь. С каждой яблони в саду упало по 2 яблока. Какой государственный язый Казахстана?', 'Казахский', 'Древнерусский', 'Казахский русский', 'Грузинский')
q3 = Question('Сколько даётся секунд на размышление?', '30', '60', '2', '20')
q4 = Question('В каком городе находится Берлинская стена?', 'Берлин', 'Калуга', 'Самара', 'Африка')
q5 = Question('Где было Ледовое побоище?', 'На льду', 'В небе', 'На земле', 'В горах')
q6 = Question('Какой государствекнный язык России?', 'Русский', 'Украинский', 'Мандалорский', 'Межгалактический')
q7 = Question('Какой может быть лампа?', 'Твердой', 'Жидкой', 'Газообразной', 'Что это')
q8 = Question('Квадратный корень из 100', '10', '100', '200', '50')
q9 = Question('Казахстан - это что?', 'Страна', 'Остров', 'Материк', 'Планета')
q10 = Question('Сколько всего здесь вопросов?', '10', '5', '20', '1000')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)

RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

button = QPushButton('Ответить')

layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

AnswerGroupBox = QGroupBox('Результат теста:')
right_answer = QLabel('Правильно')
answer1 = QLabel('Правильный ответ')
layoutv2 = QVBoxLayout()
layoutv2.addWidget(right_answer, alignment = Qt.AlignCenter)
layoutv2.addWidget(answer1, alignment = Qt.AlignCenter)
AnswerGroupBox.setLayout(layoutv2)
AnswerGroupBox.hide()

layout2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layout2.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
layout3.addWidget(button, alignment = Qt.AlignCenter)

layout1.addWidget(lb_question, alignment = Qt.AlignCenter)

layout_main.addLayout(layout1)
layout_main.addLayout(layout2)
layout_main.addLayout(layout3)
Radio1GroupBox = QButtonGroup()
Radio1GroupBox.addButton(rbtn_1)
Radio1GroupBox.addButton(rbtn_2)
Radio1GroupBox.addButton(rbtn_3)
Radio1GroupBox.addButton(rbtn_4)

button.clicked.connect(click_OK)
my_win.score = 0
my_win.total = 0
next_question()
my_win.setLayout(layout_main)
my_win.show()


app.exec_()