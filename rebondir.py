from tkinter import *
import random
import time

tk = Tk()
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-0.005, -0.0025, 0, 0.0025, 0.05]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -0.0025
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        pass
        
ball = Ball(canvas, 'red')

def move():
    canvas.move(ball.id,1,0) #fonction pour deplacer l'objet

while 1:
    ball.draw()
    move()
    tk.update()
    tk.update_idletasks()
    time.sleep(0.005)
