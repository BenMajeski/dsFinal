#benjamin majeski
#ds final
#this project will be working with trees and lists

import tkinter as tk
#this function is for later round of questions
def fRound(question):
    root = tk.Tk()
    root.title("Second round")

    question_label = tk.Label(root, text=question.prompt)
    question_label.pack()

    var = tk.StringVar(value=question.answer[0])

    def submit_answer():
        selected_answer = var.get()
        root.destroy()
        return selected_answer

    for idx, option in enumerate(question.answer, start=1):
        tk.Radiobutton(root, text=option, variable=var, value=option).pack()

    submit_button = tk.Button(root, text="Submit", command=submit_answer)
    submit_button.pack()

    root.mainloop()

    # Return the selected answer
    return var.get()


def submit_answer(window):
    window.destroy()


class Question:
    def __init__(self, prompt, answer, answerchange):
        self.prompt = prompt
        self.answer = answer
        self.achange = answerchange

class sQuestion:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        self.game = None

class Tree:
    def __init__(self, data, game=None):
        self.left = None
        self.right = None
        self.data = data
        self.game = game

class Score:
    def __init__(self):
        self.score = 0

    def QuizQuestion(self, question):
        answer_window = tk.Tk()
        answer_window.title("Recommendation Quiz")

        tk.Label(answer_window, text=question.prompt).pack()

        var = tk.StringVar(value=question.answer[0])
        for idx, option in enumerate(question.answer, start=1):
            tk.Radiobutton(answer_window, text=option, variable=var, value=option).pack()

        tk.Button(answer_window, text="Submit",
                  command=lambda: self.submit_answer(answer_window, question, var.get())).pack()

        answer_window.mainloop()

    def submit_answer(self, window, question, selected_answer):
        for idx, option in enumerate(question.answer, start=1):
            if selected_answer == option:
                self.score += question.achange[idx - 1]

        window.destroy()

    def display(self):
        return str(self.score)

def gamerTree():
    q = [
        sQuestion("do you like shooters?", ["yes", "no"]),
        sQuestion("do you like racing", ["yes", "no"]),
        sQuestion("do you like battle royals?", ["yes", "no"])
    ]

    gTree = Tree(q[0])
    gTree.left = Tree(q[1])
    gTree.right = Tree(q[2])
    gTree.right.right = Tree(None, 'Fortnite')

    gTree.right.left = Tree(None, 'Call of duty')

    gTree.left.right = Tree(None, 'Rocket League')

    gTree.left.left = Tree(None, 'League of Legends')

    selected_answer = ""
    while gTree.data is not None:
        selected_answer = fRound(gTree.data)


        if selected_answer == "yes":
            gTree = gTree.right
        else:
            gTree = gTree.left

    result_window = tk.Tk()
    result_window.title("Result")

    result_label = tk.Label(result_window, text="Your ideal game is " + gTree.game)
    result_label.pack()

    result_window.mainloop()

def middleTree():
    q = [
        sQuestion("do you like Platformers?", ["yes", "no"]),
        sQuestion("do you prefer older games?", ["yes", "no"]),
        sQuestion("would you rather go to a concert or a football game?", ["concert", "football"])
    ]
    gTree = Tree(q[0])
    gTree.left = Tree(q[1])
    gTree.right = Tree(q[2])
    gTree.left.left = Tree(None, 'Super Mario Bros 3')

    gTree.left.right = Tree(None, 'Super Mario Wonder')

    gTree.right.left = Tree(None, 'Dance Dance Revolution')

    gTree.right.right = Tree(None, 'Madden 24')

    selected_answer = ""
    while gTree.data is not None:
        selected_answer = fRound(gTree.data)

        if selected_answer == "yes":
            gTree = gTree.left
        else:
            gTree = gTree.right

    result_window = tk.Tk()
    result_window.title("Result")

    result_label = tk.Label(result_window, text="Your ideal game is " + gTree.game)
    result_label.pack()

    result_window.mainloop()

def nonGamerTree():
    q = [
        sQuestion("do you prefer Puzzles or sports?", ["Puzzles", "Sports"]),
        sQuestion("do you handle stress well?", ["yes", "no"]),
        sQuestion("do you like physical activity?", ["yes", "no"])
    ]
    gTree = Tree(q[0])
    gTree.left = Tree(q[1])
    gTree.right = Tree(q[2])
    gTree.left.right = Tree(None, 'Tetris')
    gTree.left.left = Tree(None, 'Candy Crush')
    gTree.right.right = Tree(None, 'Wii Sports')
    gTree.right.left = Tree(None, 'Chess')

    selected_answer = ""
    while gTree.data is not None:
        selected_answer = fRound(gTree.data)

        if selected_answer == "yes":
            gTree = gTree.right
        else:
            gTree = gTree.left

    result_window = tk.Tk()
    result_window.title("Result")

    result_window = tk.Tk()
    result_window.title("Result")

    result_label = tk.Label(result_window, text="Your ideal game is " + gTree.game)
    result_label.pack()

    result_window.mainloop()


points = Score()
points.QuizQuestion(Question("how much time do you have to play video games?", ["a lot", "a good amount", "not a lot", "barely any at all!"], [3, 1, -1, -3]))

points.QuizQuestion(Question("do you have a lot of friends who like to play games?", ["a lot", "a good amount", "not a lot", "barely any at all!"], [1, 0, -1, -2]))

points.QuizQuestion(Question("have you played a lot of games in your life?", ["a lot", "a good amount", "not a lot", "barely any at all!"], [3, 1, -1, -3]))

points.QuizQuestion(Question("how much do you long complicated stories in games?", ["I love them", "sure", "eh", "not my cup of tea"], [3, 1, -1, -3]))

points.QuizQuestion(Question("would you consider yourself to be quite competitive?", ["very much so", "on occasion", "not really", "I dislike competition"], [3, 1, -1, -3]))

points.QuizQuestion(Question("which book would you rather read?", ["animal farm", "Charlotte's web", "twilight", "Christmas carol"], [2, 1, -1, -1]))

points.QuizQuestion(Question("what would be your favorite type of party?", ["Costume party", "Fancy party", "Tailgate party", "I don't like parties"], [0, 3, -3, 1]))

points.QuizQuestion(Question("which of these would you most want to travel to", ["france", "hawaii", "tokyo", "toronto"], [2, -2, 3, -1]))


#takes the first part of the quiz into account to give you more custom answers
if points.score > 3:
    gamerTree()
elif points.score > -4:
    middleTree()
else:
    nonGamerTree()


