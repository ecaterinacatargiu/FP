from tkinter import *
from tkinter import messagebox
from Entities.Game import Game
from Entities.Square import Square
from Entities.Board import Board


class ObstructionGUI:

    def startGUI(self):
        self.root = Tk()
        self.root.title("Assignment10 - Obstruction Game")
        self.root.configure(background="white")

        """Text entry box"""

        self.frameRC = Frame(self.root)
        self.frameRC.pack(side = TOP)

        self.row1 = Label(self.frameRC, text="Rows: ", bg="papaya whip")
        self.row1.pack(side=LEFT)

        self.row_entry = Entry(self.frameRC, width=15)
        self.row_entry.pack(side=LEFT)

        self._col1 = Label(self.frameRC, text="Columns: ", bg ="papaya whip")
        self._col1.pack(side = LEFT)

        self.col1_entry = Entry(self.frameRC, width=15)
        self.col1_entry.pack(side = LEFT)


        self.frameOption = Frame(self.root)
        self.frameOption.pack(side=TOP)

        self.row2 = Label(self.frameOption, text="So, who's first? ", bg='papaya whip')
        self.row2.pack(side=LEFT)

        self.option_entry = Entry(self.frameOption, width = 15)
        self.option_entry.pack(side=LEFT)

        """Board repesentation"""

        self.frameBoard = Frame(self.root)
        self.frameBoard.pack()

        self.buttonP = Button(self.frameBoard, compound = CENTER, text = "OBSTRUCTION - START GAME", bg="papaya whip", command=self.PlayObstruction)
        self.buttonP.pack()

        self.root.mainloop()


    def PlayObstruction(self):

        self.frame_2 = Frame(self.root)
        self.frame_2.pack()



        try:
            self._rows = int(self.row_entry.get())
            self._columns = int(self.col1_entry.get())
            self.o = int(self.option_entry.get())
            if int(self.o) != 1 and int(self.o) != 2:
                raise ValueError("Please enter 1 or 2!")

            self.frameRC.pack_forget()
            self.frameBoard.pack_forget()
            self.frameOption.pack_forget()

            self.board = Board(self._rows, self._columns)
            self._game = Game(self.board)

            self.buttons = []

            c = 0
            for row in range(1,self._rows+1):
                for col in range(1,self._columns+1):
                    self.buttons.append(Button(self.frame_2, text=" ", width=3, height=1, bg="misty rose", command=lambda col=col, row=row: self._move_first(row, col)))
                    self.buttons[c].grid(column=col, row=row)
                    c += 1
            if self.o == 2:
                self._game.runAIPlayer(self._rows, self._columns)
                self._change()

        except Exception as e:
            messagebox.showerror("Error!", str(e))




    def _move_first(self, row, col):

        try:

            self._game.moveHuman(Square(row, col), self._rows, self._columns)

            self._change()


            if self.board.gameWon(self._rows, self._columns):
                messagebox.showinfo("Game is won!", "You won!Finally")
                self.root.destroy()

            else:
                self._game.runAIPlayer(self._rows, self._columns)
                self._change()
                if self.board.gameWon(self._rows, self._columns):
                    messagebox.showinfo("Game is won!", "AI won the game! Again...")
                    self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error!", str(e))


    def _change(self):
        count = 0
        for r in range(1,self._rows+1):
            for c in range(1,self._columns+1):
                if self.board.getSquare(r-1, c-1) == "*":
                    self.buttons[count].config(bg="thistle2")
                else:
                    self.buttons[count].config(text=self.board.getSquare(r-1, c-1))
                count += 1



