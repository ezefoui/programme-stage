from tkinter import *
import random
import time
import tkinter.font as tkFont


tk = Tk()
tk.resizable(0, 0)
tk.wm_attributes("-fullscreen", 1)
canvas = Canvas(tk, width=1300, height=800, bd=0, highlightthickness=0)
canvas.configure(bg="black")
canvas.pack()
tk.update()
score = 0
score_display = canvas.create_text(190, 40, text=f"Score: {score}", font=("Press Start 2P", 32), fill="white")
game_over_text = None
game_running = True

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(45, 45, 90, 90, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-8, -4, -2, 2, 4, 8]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -8
        self.speed_multiplier = 1.25
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        global score
        self.canvas.move(self.id, self.x * self.speed_multiplier, self.y * self.speed_multiplier)
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
            self.speed_multiplier = min(self.speed_multiplier + 0.2, 10)

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
        game_over_text = canvas.create_text(650, 400, text="GAME OVER", font=("Press Start 2P", 96), fill="white")
        tk.update()
        tk.after(5000) 
        tk.quit()

 
class Rectangle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 30, width=0, fill=color)
        self.canvas.move(self.id, 650, 500)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.small_rect = canvas.create_rectangle(0, 0, 125, 10, fill="black")
        self.canvas.move(self.small_rect, 25, 10)
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
        self.canvas.coords(self.small_rect, pos[0] + 13, pos[1] +10, pos[0] + 138, pos[1] + 20)

    def move_left(self, event):
        self.x = -6  # Vitesse à gauche

    def move_right(self, event):
        self.x = 6  # Vitesse à droite


ball = Ball(canvas, 'white')
rectangle = Rectangle(canvas, 'white')


while 1:
    ball.draw()
    rectangle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)