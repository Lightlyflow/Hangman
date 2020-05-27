import tkinter as tk
from string import ascii_uppercase


class Hangman:
    def __init__(self):
        # Variables
        self.root = tk.Tk()
        self.picture_frame = None
        self.button_frame = None
        self.word_frame = None

        # Modifying stuff
        self.root.title("Hangman")
        self.root.geometry("1000x700")
        self.root.resizable(width=0, height=0)

        # Methods to run
        self.initBoard()
        self.root.mainloop()

    def initBoard(self):
        self.createPictureFrame()
        self.createButtonFrame()
        self.createWordFrame()

        print("Cell size: " + str(self.root.size()))
        self.root.columnconfigure(0, minsize=400)
        self.root.columnconfigure(1, minsize=600)
        self.root.rowconfigure(0, minsize=200)
        self.root.rowconfigure(1, minsize=500)
        return

    def createPictureFrame(self):
        self.picture_frame = tk.Frame(master=self.root)
        self.picture_frame["bg"] = "blue"
        self.picture_frame.grid(row=0, column=0, rowspan=2, sticky="NSEW")

        self.pf_label = tk.Label(master=self.picture_frame, text="Picture (Canvas) Frame")
        self.pf_label.pack()
        return

    def createButtonFrame(self):
        self.button_frame = tk.Frame(master=self.root)
        self.button_frame["bg"] = "green"
        self.button_frame.grid(row=1, column=1, sticky="NSEW")

        """
        TODO
        """
        # for letter in ascii_uppercase[:10]:
        #     button = tk.Button(master=self.button_frame, text=letter)
        #     button.pack(side=tk.LEFT)
        return

    def createWordFrame(self):
        self.word_frame = tk.Frame(master=self.root)
        self.word_frame["bg"] = "yellow"
        self.word_frame.grid(row=0, column=1, sticky="NSEW")

        self.wf_label = tk.Label(master=self.word_frame, text="[Word goes here!]")
        self.wf_label.config(font=("Times new roman", 50))
        self.wf_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        return


if __name__ == "__main__":
    game = Hangman()
