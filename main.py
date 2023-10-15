import tkinter as tk


def end_check(matrix, size):
    return False


def win_check(matrix, size):
    return False


window = tk.Tk()
window.title("2048")
window.geometry('300x420')
canvas = tk.Canvas(window, width=245, height=245, bg="gray")
for i in range(1, 5):
    for j in range(1, 5):
        canvas.create_rectangle(5*j + 55*(j-1), 5*i + 55*(i-1), 5*j + 55*j, 5*i + 55*i, fill="white")
        canvas.create_text(5*j + 55*(j-1) + 28, 5*i + 55*(i-1) + 28, text="2048", font="calibre", justify="center",
                           fill="black")
canvas.pack()
btn1 = tk.Button(window, text="Вверх", bg="green")
btn1.place(x=100, y=250, width=100, height=50)
btn2 = tk.Button(window, text="Вниз", bg="green")
btn2.place(x=100, y=305, width=100, height=50)
btn3 = tk.Button(window, text="Влево", bg="green")
btn3.place(x=45, y=250, width=50, height=105)
btn4 = tk.Button(window, text="Вправо", bg="green")
btn4.place(x=205, y=250, width=50, height=105)
btn1 = tk.Button(window, text="Перезапустить игру", bg="green")
btn1.place(x=45, y=360, width=210, height=50)
tk.Button()
window.mainloop()
