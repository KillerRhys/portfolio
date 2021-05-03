from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title('Quiz Bowl')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
             150,
             125,
             width=280,
             text='test question',
             fill=THEME_COLOR,
             font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        timg = PhotoImage(file='images/true.png')
        fimg = PhotoImage(file='images/false.png')
        self.true_button = Button(image=timg, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=fimg, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(column=0, row=3)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg='orange')
            self.canvas.itemconfig(self.question_text, text=f"You've finished the quiz with a {self.quiz.score} / {len(self.quiz.question_list)}")

    def true_pressed(self):
        self.a_check(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.a_check(self.quiz.check_answer('False'))

    def a_check(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)