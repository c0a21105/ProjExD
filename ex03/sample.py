import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr,jid
    label["text"] = tmr
    tmr += 1
    #root.after(1000, count_up)
    jid = root.after(1000, count_up)

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

def key_down(event):
    global jid
    if jid is not None:
        root.after_cancel(jid)
        jid = None
    key = event.keysym
    jid = root.after(1000, count_up)
    #root.after(1000, count_up)
    tkm.showinfo("キー押下", f"{key}キーが押されました。")

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, font=("", 80))
    label.pack()

    tmr = 0
    jid = None
    #count_up()

    root.bind("<KeyPress>", key_down)
    button = tk.Button(root, text="押すな")
    button.bind("<1>", button_click)
    button.pack()

    root.mainloop()