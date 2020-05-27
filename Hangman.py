import tkinter as tk


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
        self.root.columnconfigure([1, 2], weight=1)
        self.root.rowconfigure([1, 2], weight=1)

        self.createPictureFrame()
        self.createButtonFrame()
        self.createWordFrame()
        return

    def createPictureFrame(self):
        self.picture_frame = tk.Frame(master=self.root, width=400, height=700)
        self.picture_frame["bg"] = "blue"
        self.picture_frame.grid(row=0, column=0, rowspan=2, sticky="NSEW")
        return

    def createButtonFrame(self):
        self.button_frame = tk.Frame(master=self.root, width=600, height=500)
        self.button_frame["bg"] = "green"
        self.button_frame.grid(row=1, column=1, sticky="NSEW")
        return

    def createWordFrame(self):
        self.word_frame = tk.Frame(master=self.root, width=600, height=200)
        self.word_frame["bg"] = "yellow"
        self.word_frame.grid(row=0, column=1, sticky="NSEW")
        return


if __name__ == "__main__":
    game = Hangman()
