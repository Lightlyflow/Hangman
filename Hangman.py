import random
import tkinter as tk
from functools import partial
from string import ascii_uppercase

# ([Word] , [Hint])
wordDictionary = {}


# Adds the words from file words.txt to var dictionary
def createDic(dictionary):
    with open("words.txt", "r") as words:
        for line in words:
            temp = line.split(", ")
            dictionary[temp[0]] = temp[1].rstrip()
    return


# Prints the content of the var dictionary out
def printDic(dictionary):
    for word in list(dictionary):
        print(str(word) + " " + str(dictionary[word]))
    return


def addToDic(dictionary):
    dictSet = set(list(dictionary))
    key = input("Word: ")
    hint = input("Hint: ")
    if key not in dictSet:
        file = open("words.txt", "a")
        file.write(str(key) + ", " + str(hint))
        file.close()
    return


class Hangman:
    def __init__(self):
        # Variables
        self.root = tk.Tk()
        self.picture_frame = None
        self.button_frame = None
        self.word_frame = None
        createDic(wordDictionary)
        # printDic(wordDictionary)

        # Prints answer
        # print("Word", self.word, "Hint", self.hint)

        # Modifying stuff
        self.root.title("Hangman")
        self.root.geometry("1000x700")
        self.root.resizable(width=0, height=0)

        # Methods to run
        self.initBoard()
        self.root.mainloop()

    def initBoard(self):
        # Initializing vars
        self.word = random.choice(list(wordDictionary))
        self.hint = wordDictionary.get(self.word)
        self.word = self.word.upper()
        self.chances = 5

        self.createPictureFrame()
        self.createButtonFrame()
        self.createWordFrame()

        self.root.columnconfigure(0, minsize=400)
        self.root.columnconfigure(1, minsize=600)
        self.root.rowconfigure(0, minsize=200)
        self.root.rowconfigure(1, minsize=500)
        return

    def createPictureFrame(self):
        self.picture_frame = tk.Frame(master=self.root, bg="blue", padx=2, pady=2)
        self.picture_frame.grid(row=0, column=0, rowspan=2, sticky="NSEW")

        self.pg_canvas = tk.Canvas(master=self.picture_frame)
        self.pg_canvas.pack(fill=tk.BOTH, expand=1)

        # At beginning, creates the stage
        self.pg_canvas.create_line(65, 79, 243, 79, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="0")
        self.pg_canvas.create_line(65, 79, 65, 611, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="0")
        self.pg_canvas.create_line(243, 79, 243, 119, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="0")
        self.pg_canvas.create_rectangle(38, 611, 340, 665, fill="black", width=4, tags="0")
        return

    def createButtonFrame(self):
        self.button_frame = tk.Frame(master=self.root, bg="green", padx=2, pady=2)
        self.button_frame.grid(row=1, column=1, sticky="NSEW")

        self.button_frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.button_frame.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)

        # Adding alphabet
        for index in range(26):
            button = tk.Button(master=self.button_frame, text=ascii_uppercase[index], font=("Times New Roman", 30))
            buttonPressAction = partial(self.buttonPress, button)
            button.config(command=buttonPressAction)
            button.grid(row=index // 6, column=index % 6, sticky="NSEW", padx=2, pady=2)

        experimentalButton = tk.Button(master=self.button_frame, text="Exp", command=lambda: self.showEndScreen(win=True))
        experimentalButton.grid(row=4, column=2, sticky="NSEW", padx=2, pady=2)
        return

    def createWordFrame(self):
        self.word_frame = tk.Frame(master=self.root, bg="yellow")
        self.word_frame.grid(row=0, column=1, sticky="NSEW")

        # Creating string to put in wf_label
        string = ""
        for i in range(len(self.word)):
            string += "_"

        # Answer box
        self.wf_label = tk.Label(master=self.word_frame, text=string, font=("terminal", 50))
        self.wf_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Hint box
        wf_hintLabel = tk.Label(master=self.word_frame, text="Hint: " + str(self.hint), font=("terminal", 20))
        wf_hintLabel.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        return

    # Bindings and commands and other functions
    def revealNextBodyPart(self):
        if self.chances < 0:
            self.showEndScreen(win=False)
        elif self.chances == 5:
            self.pg_canvas.create_oval(167, 119, 308, 250, width=4, tags="Head")
        elif self.chances == 4:
            self.pg_canvas.create_line(237, 250, 237, 447, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="Body")
        elif self.chances == 3:
            self.pg_canvas.create_line(237, 319, 293, 296, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="HandR")
            self.pg_canvas.create_line(237, 319, 187, 296, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="HandL")
        elif self.chances == 2:
            self.pg_canvas.create_line(237, 447, 292, 510, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="LegR")
            self.pg_canvas.create_line(237, 447, 182, 510, width=4, joinstyle=tk.BEVEL, capstyle=tk.ROUND, tags="LegL")
        elif self.chances == 1:
            self.pg_canvas.create_line(196, 162, 225, 181, width=4, capstyle=tk.ROUND, tags="EyeL1")
            self.pg_canvas.create_line(225, 162, 196, 181, width=4, capstyle=tk.ROUND, tags="EyeL2")
            self.pg_canvas.create_line(246, 162, 277, 181, width=4, capstyle=tk.ROUND, tags="EyeR1")
            self.pg_canvas.create_line(277, 162, 246, 181, width=4, capstyle=tk.ROUND, tags="EyeR2")
        elif self.chances == 0:
            self.pg_canvas.create_arc(204, 208, 266, 228, width=4, extent=180, tags="Mouth")

        self.chances -= 1
        return

    def buttonPress(self, button):
        letter = button["text"]
        button["state"] = tk.DISABLED
        included = False
        for index in range(len(self.word)):
            if self.word[index] == letter:
                iword = self.wf_label["text"]
                self.wf_label["text"] = iword[:index] + letter + iword[index + 1:]
                included = True
        if not included:
            self.revealNextBodyPart()
        elif self.wf_label["text"].find("_") == -1:
            self.showEndScreen(win=True)
        return

    def playAgainYes(self):
        self.removeAll()
        print("yes")
        self.initBoard()
        return

    def playAgainNo(self):
        print("No")
        self.removeAll()
        frame = tk.Frame(master=self.root, bg="#EBCA37")
        labelTY=tk.Label(master=frame, width=200, height=200, text="Thank You For Playing!", bg="#EBCA37")
        labelTY.config(font=("Ariel", 30))
        frame.pack(fill=tk.BOTH, expand=1)
        labelTY.pack()
        self.root.after(3000, lambda: self.root.destroy())
        return

    def showEndScreen(self, win):
        self.removeAll()

        frame = tk.Frame(master=self.root, background="#EBCA37")
        label = tk.Label(master=frame, text="Do you want to play again?", background="#83C8F1")
        label.config(font=("Ariel", 18))
        if(win):
            labelResult = tk.Label(master=frame, text="YOU WON!", background="#EBCA37")
        else:
            labelResult = tk.Label(master=frame, text="YOU LOST!", background="#EBCA37")

        labelResult.config(font=("Ariel", 35))
        bYes = tk.Button(master=frame, text="Yes", background="#5FDE35", command=self.playAgainYes)
        bYes.config(font=("Ariel", 20))
        bNo = tk.Button(master=frame, text="No", background="#F36B46", command=self.playAgainNo)
        bNo.config(font=("Ariel", 20))
        frame.pack(fill=tk.BOTH)

        label.grid(row=2, column=2, columnspan=2, sticky="NSEW")
        bYes.grid(row=3, column=2, sticky="NSEW")
        bNo.grid(row=3, column=3, sticky="NSEW")
        labelResult.grid(row=0, column=2, columnspan=2, sticky="NSEW")

        frame.columnconfigure(index=[0, 1, 2, 3, 4, 5], weight=1, minsize=166)
        frame.rowconfigure(index=[0, 1, 2, 3, 4], weight=1, minsize=140)
        return

    def removeAll(self):
        for obj in self.root.winfo_children():
            obj.destroy()


if __name__ == "__main__":
    game = Hangman()
