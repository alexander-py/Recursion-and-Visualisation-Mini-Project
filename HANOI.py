from turtle import *
import time
import sys
from tkinter import *
from tkinter import ttk
import tkinter.simpledialog


game = input("Please choose a version =")
if game ==("Recursive"):
    root = Tk() #Code would not work without these 3 lines(?)
    w = Label(root, text="Dialog Practice")
    w.pack()
    root.withdraw()  #Removes tk popup window
    number = tkinter.simpledialog.askstring("So, how many?", "Tell us how many discs you want today (min=0;max=10)")
    title("The Towers of Hanoi by ALEXANDER STEFANOV / Student ID:XXXXXXX")


    class Disc(Turtle):
        def __init__(self, n):
            Turtle.__init__(self, shape="square", visible=False)
            self.speed(10 - n)
            self.pu()
            self.shapesize(1.5, n*1.5, 2) # square-->rectangle
            self.fillcolor(n/10., 0, 1-n/10.) #max 10 discs
            self.st()
            self.move = 0


    class Tower(list):
        "Hanoi tower, a subclass of built-in type list"
        def __init__(self, x):
            "create an empty tower. x is x-position of peg"
            self.x = x
        def push(self, d):
            d.clear()
            d.setx(self.x)
            d.sety(-150+34*len(self))
            self.append(d)
            d.write("moves = " + str(d.move),
            align = "center", font = ("Courier", 16, "bold"))
            d.move+=1
        def pop(self):
            d = list.pop(self)
            d.sety(150)
            return d


    moves = 0

    def hanoi(n, from_, with_, to_):
        global moves
        if int(n) > 0:
            hanoi(int(n)-1, from_, to_, with_)
            moves += 1
            to_.push(from_.pop())
            hanoi(int(n)-1, with_, from_, to_)
        clear()
        write("Total moves = "+ str(moves),
              align="center", font=("Courier", 16, "bold"))
        mpb.pack()
        mpb["maximum"] = 100
        mpb["value"] = 100 * (moves / (2 ** int(number) - 1))


    def play():
        onkey(None,"space")
        clear()
        global mpb
        mGui = Tk() #Implementing tkinter

        mGui.title('Towers of Hanoi PROGRESS')

        mpb = ttk.Progressbar(mGui, orient="horizontal", length=500, mode="determinate")

        hanoi(number, t1, t2, t3)
        sety(-250)
        write("press STOP button to exit or simply press q",
              align="center", font=("Courier", 16, "bold"))

    def pause():
        time.sleep(3)

    def quit():
        onkey(None,"q")
        bye()

    def main():
        global t1, t2, t3, mpb
        ht(); penup(); goto(0, -225)   # writer turtle
        t1 = Tower(-250)
        t2 = Tower(0)
        t3 = Tower(250)
        # make tower of 6 discs
        for i in range(int(number),0,-1):
            t1.push(Disc(i))
        # prepare spartanic user interface 😉
        write("ALEXANDER STEFANOV's ToH. Press spacebar to start game",
              align="center", font=("Courier", 16, "bold"))
        onkey(play, "space")
        sety(-260) #Testing alignment
        write("Press p to Pause",
              align="center", font=("Courier", 16, "bold"))
        onkey(pause, "p")
        sety(-300) #Testing alignment
        write("Press q to Quit",
              align="center", font=("Courier", 16, "bold"))
        onkey(quit, "q")
        listen()
        return "EVENTLOOP"

    if __name__=="__main__":
        msg = main()
        print(msg)
        mainloop()

elif game ==("NonRecursive"):
    root = Tk()
    w = Label(root, text="Dialog Practice")
    w.pack()
    root.withdraw()  # removes tk popup window
    number = tkinter.simpledialog.askstring("So, how many?", "Tell us how many discs you want today (min=0;max=10)")
    title("The Towers of Hanoi by ALEXANDER STEFANOV / Student ID:XXXXXXX")


    class Disc(Turtle):
        def __init__(self, n):
            Turtle.__init__(self, shape="square", visible=False)
            self.speed(10 - n)
            self.pu()
            self.shapesize(1.5, n*1.5, 2) # square-->rectangle
            self.fillcolor(n/10., 0, 1-n/10.) #max 10 discs
            self.st()
            self.move = 0


    class Tower(list):
        "Hanoi tower, a subclass of built-in type list"
        def __init__(self, x):
            "create an empty tower. x is x-position of peg"
            self.x = x
        def push(self, d):
            d.clear()
            d.setx(self.x)
            d.sety(-150+34*len(self))
            self.append(d)
            d.write("moves = " + str(d.move),
            align = "center", font = ("Courier", 16, "bold"))
            d.move+=1
        def pop(self):
            d = list.pop(self)
            d.sety(150)
            return d


    moves = 0

    #NOT FINISHED/ BUG NOT FIXED WHEN VERSION IS NONREC
    def nonr_move(X, Y):
        if not len(X):
            X.push(Y.pop())
        elif not len(Y):
            Y.push(X.pop())
        elif X[-1] > Y[-1]:
            X.push(Y.pop())
        else:
            Y.push(X.pop())


    def hanoi_nonr(n, X, Y, Z):
        global moves
        if int(n) % 2 == 0:
            Y, Z = Z, Y
        for i in range(1, 2 ** int(n)):
            if i % 3 == 1:
                nonr_move(X, Z)
            if i % 3 == 2:
                nonr_move(X, Y)
            if i % 3 == 0:
                nonr_move(Y, Z)
            moves += 1


    def hanoi(n, from_, with_, to_):
        global moves
        if int(n) > 0:
            hanoi(int(n)-1, from_, to_, with_)
            moves += 1
            to_.push(from_.pop())
            hanoi(int(n)-1, with_, from_, to_)
        clear()
        write("Total moves = "+ str(moves),
              align="center", font=("Courier", 16, "bold"))
        mpb.pack()
        mpb["maximum"] = 100
        mpb["value"] = 100 * (moves / (2 ** int(number) - 1))


    def play():
        onkey(None,"space")
        clear()
        global mpb
        mGui = Tk()

        mGui.title('Towers of Hanoi PROGRESS')

        mpb = ttk.Progressbar(mGui, orient="horizontal", length=500, mode="determinate")

        hanoi_nonr(number, t1, t2, t3)
        sety(-250)
        write("press STOP button to exit or simply press q",
              align="center", font=("Courier", 16, "bold"))

    def pause():
        time.sleep(3)

    def quit():
        onkey(None,"q")
        bye()

    def main():
        global t1, t2, t3, mpb
        ht(); penup(); goto(0, -225)   # writer turtle
        t1 = Tower(-250)
        t2 = Tower(0)
        t3 = Tower(250)
        # make tower of 6 discs
        for i in range(int(number),0,-1):
            t1.push(Disc(i))
        # prepare spartanic user interface 😉
        write("ALEXANDER STEFANOV's ToH. Press spacebar to start game",
              align="center", font=("Courier", 16, "bold"))
        onkey(play, "space")
        sety(-260)
        write("Press p to Pause",
              align="center", font=("Courier", 16, "bold"))
        onkey(pause, "p")
        sety(-300)
        write("Press q to Quit",
              align="center", font=("Courier", 16, "bold"))
        onkey(quit, "q")
        listen()
        return "EVENTLOOP"

    if __name__=="__main__":
        msg = main()
        print(msg)
        mainloop()
else:
    print ("You have chosen a non-existing mode. Please , try again.")

