"""
пробный калькулятор
"""

import tkinter as tk

root = tk.Tk()

root.geometry('350x450')
root.title('calculator')

lable = tk.Label(root, width=250, height=5, background="white")
lable.pack(padx=1, pady=1)

result = ("")


def insert_value(value):
    global lable, result
    result += f"{value}"
    lable.config(text=result)

    print(result)


def maths():
    global lable, result
    num1 = ''
    num2 = ''
    if result.__contains__("="):
        if result.__contains__("+"):
            for i in range(len(result)):
                if result[i].__contains__("+"):
                    num1 += result[:i]
                    num2 += result[i+1:].strip("=")
                    out = str(int(num1) + int(num2))

    lable.config(text=out)

def init():
    frame_top = tk.Frame(root, width=350, height=100, background='black')
    frame_bottom_left = tk.Frame(root, width=300, height=350, background='gray')
    frame_bottom_right = tk.Frame(root, width=100, height=350, background='white')
    return [frame_top, frame_bottom_left, frame_bottom_right]


def gui():
    frame_bottom_left = init()
    frame_bottom_left[1].pack(side="left", padx=10, pady=15)
    frame_bottom_right = init()
    frame_bottom_right[2].pack(side="right", padx=10, pady=15)
    col = 0
    row = 0
    for step in range(10):
        button = tk.Button(frame_bottom_left[1], text=step, width=8, height=4, command=lambda value=str(step):insert_value(value))
        button.grid(row=row, column=col)
        col += 1
        if col == 3:
            col = 0
            row += 1


    operations = ["+", "-", "*", "%", "="]
    for step in range(5):
        button = tk.Button(frame_bottom_right[2], text=operations[step], width=7, height=3, command=lambda value=str(operations[step]):insert_value(value))
        button.grid(row=step, column=1)




gui()

root.mainloop()