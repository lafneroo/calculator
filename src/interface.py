"""
пробный калькулятор
"""

import tkinter as tk

root = tk.Tk()

root.geometry('350x450')
root.title('calculator')

def insert_value():
    pass



def init():
    frame_top = tk.Frame(root, width=350, height=100, background='black')
    frame_bottom_left = tk.Frame(root, width=300, height=350, background='gray')
    frame_bottom_right = tk.Frame(root, width=100, height=350, background='white')
    return [frame_top.pack(side="top"), frame_bottom_left, frame_bottom_right.pack(side="right")]


def gui():
    frame_bottom_left = init()
    frame_bottom_left[1].pack(side="left", padx=10, pady=15)
    col = 0
    row = 0
    for button in range(10):
        button = tk.Button(frame_bottom_left[1], text=str(button), width=8, height=4, command=insert_value)
        button.grid(row=row, column=col)
        col += 1
        if col == 3:
            col = 0
            row += 1



gui()

root.mainloop()