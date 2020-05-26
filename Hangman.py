import tkinter as tk


class Hangman:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman")
        self.root.geometry("700x700")
        self.initBoard()
        self.root.mainloop()

    def initBoard(self):
        self.createPictureFrame()
        self.createButtonFrame()
        self.createWordFrame()
        return

    def createPictureFrame(self):
        return

    def createButtonFrame(self):
        return
    def createWordFrame(self):
        return


if __name__ == "__main__":
    print("Ran.")
    game = Hangman()
