import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Right":
        mx += 1
    elif key == "Left":
        mx -= 1
    cx = mx*100+50
    cy = my*100+50
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500, height=900, bg="black")
    canvas.pack()

    maze = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze)

    image = tk.PhotoImage(file="fig/2.png")
    mx = 1
    my = 1
    cx = mx*100+50
    cy = my*100+50
    canvas.create_image(cx, cy, image=image, tag="koukaton")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()