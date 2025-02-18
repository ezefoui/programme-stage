from tkinter import *
import random
import time

tk = Tk()
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -0.3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Rectangle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 15, width=0, fill=color)
        self.canvas.move(self.id, 350, 250)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # Lier les touches du clavier pour contrôler le rectangle
        self.canvas.bind_all('<Left>', self.move_left)
        self.canvas.bind_all('<Right>', self.move_right)
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # Empêcher le rectangle de sortir des bords
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def move_left(self, event):
        self.x = -3  # Vitesse à gauche

    def move_right(self, event):
        self.x = 3  # Vitesse à droite

        
ball = Ball(canvas, 'red')
rectangle = Rectangle(canvas, 'blue')


while 1:
    ball.draw()
    rectangle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)