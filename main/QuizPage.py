import tkinter as tk
from db_service import DataBaseService
from random import randint

LARGE_FONT= ("Verdana", 20)

class QuizPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db_service = DataBaseService()

        self.label = tk.Label(self)
        self.label.place(x=10,y=10)

        self.variant1 = tk.Label(self)
        self.variant1.place(x=50, y = 620)
        self.variant1.bind('<Button-1>',lambda event,answerLabel=self.variant1:self.check_answer(event,answerLabel))

        self.variant2 = tk.Label(self)
        self.variant2.place(x=50, y=680)
        self.variant2.bind('<Button-1>',lambda event,answerLabel=self.variant2:self.check_answer(event,answerLabel))

        self.variant3 = tk.Label(self)
        self.variant3.place(x=650, y=620)
        self.variant3.bind('<Button-1>',lambda event,answerLabel=self.variant3:self.check_answer(event,answerLabel))

        self.variant4 = tk.Label(self)
        self.variant4.place(x=650, y=680)
        self.variant4.bind('<Button-1>',lambda event,answerLabel=self.variant4:self.check_answer(event,answerLabel))

        self.used_movies = set()
        self.score = 0
        self.current_correct_answer = None
        self.mistakes = 1

        self.set_new_question()

    def set_new_question(self):
        rnd_index = randint(0,3)
        answers = self.db_service.get_variants()
        new_question = self.db_service.get_random_movie()

        if new_question in self.used_movies:
            while new_question in self.used_movies:
                new_question = self.db_service.get_random_movie()
        else:
            if new_question in answers:
                while new_question in answers:
                    new_question = self.db_service.get_random_movie()
            else:
                self.used_movies.add(new_question)
                self.current_correct_answer = new_question[1]
                answers.add(new_question)

        self.variant1.config(text=answers.pop()[1])
        self.variant2.config(text=answers.pop()[1])
        self.variant3.config(text=answers.pop()[1])
        self.variant4.config(text=answers.pop()[1])
        img = tk.PhotoImage(file = new_question[3])
        self.label.photo = img
        self.label.config(image=img)
        print(self.current_correct_answer)

    def check_answer(self,event,answerLabel):

        if answerLabel['text'] == self.current_correct_answer:
            self.score += 1
            self.set_new_question()
        else:

            game_over = tk.Message(self,text='Game over, your score:{}'.format(self.score))
            game_over.pack()
