import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(width=1500, height=900, bg="black")
    canvas.pack()

    image = tk.PhotoImage(file="fig/2.png")

    cx = 300
    cy = 400
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<keyRelease>", key_up)

    root.mainloop()