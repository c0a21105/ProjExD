import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
from datetime import datetime

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def count_down():
    global jid, count, st
    label["text"] = "スタートまで"
    label.place(x=750,y=100,anchor=tk.CENTER)
    label2["text"] = count
    label2.place(x=750,y=200,anchor=tk.CENTER)
    count-=1
    if count < 0:
        label.place_forget()
        label2.place_forget()
        st = datetime.now()
        jid = root.after(10, main_proc)
    jid = root.after(1000, count_down)

def main_proc():
    global mx, my, jid
    if jid != None:
        root.after_cancel(jid)
        jid = None

    if key == "Up" and maze[mx][my-1] == 0:
        my -= 1
    elif key == "Down" and maze[mx][my+1] == 0:
        my += 1
    elif key == "Right" and maze[mx+1][my] == 0:
        mx += 1
    elif key == "Left" and maze[mx-1][my] == 0:
        mx -= 1
    cx = mx*100+50
    cy = my*100+50
    canvas.coords("koukaton", cx, cy)

    print(mx, my, key, jid)
    jid = root.after(100, main_proc)

    if mx == 13 and my == 7:
        game_clear()

def game_clear():
    global jid
    ed = datetime.now()
    if jid is not None:
        root.after_cancel(jid)
        jid = None
    tkm.showinfo("おめでとう！", f"あなたは {(ed-st).seconds} 秒で迷えるこうかとんを救いました！")
    ret = tkm.askquestion("迷えるこうかとん", "もう一度プレイしますか？")
    if ret == "yes":
        jid = root.after(1, reset)
    else:
        root.destroy()

def reset():
    global mx, my, key, jid, count, maze, label, label2, image

    image = tk.PhotoImage(file="fig/2.png")

    label = tk.Label(root, font=("", 80), bg="white")
    label2 = tk.Label(root, font=("", 100), bg="white")

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    maze = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze)

    canvas.create_rectangle(100, 100, 200, 200, fill="#ff6b6b")
    canvas.create_rectangle(1300, 700, 1400, 800, fill="#8bff85")

    mx = 1
    my = 1
    cx = mx*100+50
    cy = my*100+50
    canvas.create_image(cx, cy, image=image, tag="koukaton")

    key = ""
    jid = None
    count = 3

    jid = root.after(10, count_down)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500, height=900, bg="black")
    canvas.pack()

    reset()

    root.mainloop()