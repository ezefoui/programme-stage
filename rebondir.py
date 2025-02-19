from tkinter import *
import random
import time


tk = Tk()
tk.resizable(0, 0)
tk.wm_attributes("-fullscreen", 1)
canvas = Canvas(tk, width=1300, height=800, bd=0, highlightthickness=0)
canvas.configure(bg="black")
canvas.pack()
tk.update()
score = 0
score_display = canvas.create_text(120, 40, text=f"Score: {score}", font=("Courier", 32), fill="yellow")
game_over_text = None
game_running = True

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(30, 30, 60, 60, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-8, -4, -2, 2, 4, 8]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -8
        self.speed_multiplier = 5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        global score
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
        if self.collision():
            self.y = -3
            self.canvas.move(self.id, 0, -5 if self.y > 0 else 5)
            score += 1  # Incrémentation du score
            canvas.itemconfig(score_display, text=f"Score: {score}")  # Mise à jour affichage du score
            self.speed_multiplier = min(self.speed_multiplier + 0.2, 5)

    def collision(self):
        ball_pos = self.canvas.coords(self.id)
        rect_pos = self.canvas.coords(rectangle.id)
        if (ball_pos[2] >= rect_pos[0] and ball_pos[0] <= rect_pos[2] and
            ball_pos[3] >= rect_pos[1] and ball_pos[1] < rect_pos[1] and self.y > 0):
            
            return True
        if (ball_pos[2] >= rect_pos[0] and ball_pos[0] <= rect_pos[2] and
                ball_pos[1] <= rect_pos[3] and ball_pos[3] > rect_pos[3] and
                self.y < 0):
            game_runnig = False
            self.show_game_over()
            return True
        return False
    
    def show_game_over(self):
        global game_over_text
        self.canvas.delete(self.id)
        rectangle.canvas.delete(rectangle.id)
        tk.update()
        game_over_text = canvas.create_text(650, 400, text="GAME OVER", font=("Courier", 96), fill="white")
        tk.update()
        tk.after(5000) 
        tk.quit()

 
class Rectangle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 30, width=0, fill=color)
        self.canvas.move(self.id, 650, 500)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<Left>', self.move_left)
        self.canvas.bind_all('<Right>', self.move_right)
        
        
    
    def draw(self):
        self.canvas.move(rectangle.id, self.x, 0)
        pos = self.canvas.coords(rectangle.id)
        # Empêcher le rectangle de sortir des bords
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def move_left(self, event):
        self.x = -5  # Vitesse à gauche

    def move_right(self, event):
        self.x = 5  # Vitesse à droite


ball = Ball(canvas, 'red')
rectangle = Rectangle(canvas, 'blue')


while 1:
    ball.draw()
    rectangle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)