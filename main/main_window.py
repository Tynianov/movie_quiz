import tkinter as tk
from QuizPage import QuizPage

LARGE_FONT= ("Verdana", 30)

class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.geometry('1200x750')
        self.title('Movie quiz game')
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, QuizPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Movie quiz", font=LARGE_FONT)
        label.place(x=140,y=100)

        button = tk.Button(self, text="Start",
                           command=lambda: controller.show_frame(QuizPage))
        button.place(x=210,y=250)


app = MainWindow()
app.mainloop()