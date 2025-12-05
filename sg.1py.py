import tkinter as tk

window = tk.Tk()
window.title("Snake Game")

canvas = tk.Canvas(window,width=400,height=400,background="black") 
canvas.pack()
box = canvas.create_rectangle(20,20,40,40,fill="yellow")

dx, dy = 20, 0

def move():
    canvas.move(box,dx,dy)
    window.after(200,move)

    x1, y1, x2, y2 = canvas.coords(box)
    if x1 < 0 or y1 < 0 or x2 > 400 or y2 > 400:
        game_over()
    else:
        window.after(200,move)


def change_dir(event):
    global dx,dy
    if event.keysym == "Up":
        dx,dy = 0, -20
    elif event.keysym == "Down":
        dx,dy = 0, 20
    elif event.keysym == "Left":
        dx,dy = -20, 0
    elif event.keysym == "Right":
        dx,dy = 20, 0

def game_over():
    canvas.create_text(200,200,text="GAME OVER",font=("Arial",24),fill="red")

    
window.bind("<Key>",change_dir)

move()

window.mainloop()