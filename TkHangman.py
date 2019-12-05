###############################################################################
# MCL's HANGMAN (GUI version)
# Version: 1.0.0
# Author: Marchel Sugi (MCLSugi)
# Init: Dec 01, 2019
# Last Update: Dec 03, 2019
###############################################################################

from tkinter import *
from random import choice


class App:
    def __init__(self, master):
        frame = Frame(master).pack()

        self.mistakes = 0
        self.word = '?'
        self.hiddenword = '_'
        self.imgnext = ''
        self.play = False

        # placeholder for game status
        self.lb_top = Label(frame, text='PRESS PLAY TO START')
        self.lb_top.configure(font='mono 16 bold', fg='white', bg='gray12')
        self.lb_top.place(relx=0.1, rely=0.15)

        # placeholder for the hidden word
        self.lb_mid = Label(frame, text='')
        self.lb_mid.configure(font='mono 32 bold', fg='pink3', bg='gray12')
        self.lb_mid.place(relx=0.1, rely=0.25)

        # placeholder for the user last guess
        self.lb_btm = Label(frame, text='')
        self.lb_btm.configure(font='mono 12', fg='white', bg='gray12')
        self.lb_btm.place(relx=0.25, rely=0.45)

        # placeholder for game-states picture (hangedman)
        self.img = PhotoImage(file='./img/0.gif')
        self.pic = Label(frame, image=self.img)
        self.pic.place(relx=0.7, rely=0.05)

        # buttons to start the game or quit the app
        self.b_play = Button(frame, text='PLAY', command=self.start)
        self.b_play.configure(bg='gray21', fg='white', font='mono 12 bold')
        self.b_play.place(relx=0.45, rely=0.85)

        self.b_quit = Button(frame, text='QUIT', command=quit)
        self.b_quit.configure(bg='gray21', fg='white', font='mono 12 bold')
        self.b_quit.place(relx=0.55, rely=0.85)

        # binding generated input buttons
        def bind(bt, c):
            bt.configure(command=lambda: self.onclick(c))

        # DRY _ my attempt to avoid creating alphabet buttons one by one
        # UX  _ generating these buttons will avoid user input error(s)
        space_y = 0.55
        for row in ('ABCDEFGHI', 'JKLMNOPQR', 'STUVWXYZ-'):
            space_x = 0.1
            for char in row:
                btn = Button(frame, text=char, width=1)
                btn.configure(bg='gray21', fg='white', font='mono 12 bold')
                btn.place(relx=space_x, rely=space_y)
                bind(btn, char)
                space_x += 0.062
            space_y += 0.075

    # set image states
    def setimage(self, mis):
        images = ('./img/0.gif', './img/1.gif', './img/2.gif', './img/3.gif',
                  './img/4.gif', './img/5.gif', './img/6.gif')
        if mis <= 6:
            # needed for tkinter image updating
            self.imgnext = PhotoImage(file=images[mis])
            self.pic.configure(image=self.imgnext)
            self.pic.image = self.imgnext

    # check user input
    def checkanswer(self, ch, chars):
        listhw = list(self.hiddenword)
        if ch in chars:
            i = 0

            # unveil character(s) on screen
            for c in chars:
                if c == ch:
                    listhw[i] = ch
                    self.hiddenword = ''.join(listhw)
                    self.lb_mid.configure(text=self.hiddenword)
                i += 1
        else:
            self.mistakes += 1

        if self.hiddenword == self.word:
            self.lb_top.configure(text="CONGRATS! YOU'VE WON.")
            self.play = False
        elif self.mistakes == 6:
            self.lb_top.configure(text="GAME OVER. YOU'RE HANGED!")
            self.lb_btm.configure(text=f'THE WORD IS: {self.word}')
            self.play = False
        else:
            pass

        self.setimage(self.mistakes)

    # buttons action
    def onclick(self, arg):
        if self.play:
            self.lb_btm.configure(text=f'LAST GUESS: {arg}')
            self.checkanswer(arg, self.word)

    # load the dictionary and chose random word
    def start(self):
        self.play = True
        self.mistakes = 0
        self.setimage(0)
        self.lb_top.configure(text='GUESS THE WORD! ')

        with open('dicti.txt') as f:
            self.word = choice(f.read().split()).upper()
            self.hiddenword = '\u2665' * len(self.word)
            self.lb_mid.configure(text=self.hiddenword)

            # !!! debug | cheatmode !!!
            # print(self.word)


# init
if __name__ == '__main__':
    root = Tk()
    root.geometry('720x480')
    root.configure(bg='gray12')
    root.resizable(width=False, height=False)
    root.title("MCLSugi HANGMAN   (1.0.0)")

    app = App(root)
    root.mainloop()
    root.destroy()

# fin 
