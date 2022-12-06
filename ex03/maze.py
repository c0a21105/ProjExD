import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Right":
        cx += 20
    elif key == "Left":
        cx -= 20
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500, height=900, bg="black")
    canvas.pack()

    image = tk.PhotoImage(file="fig/2.png")
    cx = 300
    cy = 400
    canvas.create_image(cx, cy, image=image, tag="koukaton")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    mm.make_maze(15, 9)

    root.mainloop()