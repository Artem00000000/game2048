import tkinter as tk
from random import randint


def end_check(matrix, size):
    return False


def win_check(matrix, size):
    return False


def generate_matrix():
    matrix: list[list[int]] = [[0 for x in range(4)] for y in range(4)]
    number = randint(1, 100)
    position1 = randint(1, 16)
    position2 = randint(1, 16)
    while position1 == position2:
        position2 = randint(1, 16)
    if number < 80:
        matrix[(position1 - 1) // 4][position1 % 4 - 1] = 2
        matrix[(position2 - 1) // 4][position2 % 4 - 1] = 2
    elif number == 80:
        matrix[(position1 - 1) // 4][position1 % 4 - 1] = 4
        matrix[(position2 - 1) // 4][position2 % 4 - 1] = 4
    else:
        matrix[(position1 - 1) // 4][position1 % 4 - 1] = 2
        matrix[(position2 - 1) // 4][position2 % 4 - 1] = 4
    return matrix


def restart():
    global matrix1
    matrix1 = generate_matrix()
    paint()


def paint():
    canvas.delete("all")
    for i in range(1, 5):
        for j in range(1, 5):
            if matrix1[i - 1][j - 1] != 0:
                canvas.create_rectangle(5 * j + 55 * (j - 1), 5 * i + 55 * (i - 1), 5 * j + 55 * j, 5 * i + 55 * i,
                                        fill="white")
                canvas.create_text(5 * j + 55 * (j - 1) + 28, 5 * i + 55 * (i - 1) + 28, text=matrix1[i - 1][j - 1],
                                   font="calibre",
                                   justify="center", fill="black")
    canvas.pack()


window = tk.Tk()
window.title("2048")
window.geometry('300x420')
matrix1 = generate_matrix()
canvas = tk.Canvas(window, width=245, height=245, bg="gray")
paint()
btn1 = tk.Button(window, text="Вверх", bg="green")
btn1.place(x=100, y=250, width=100, height=50)
btn2 = tk.Button(window, text="Вниз", bg="green")
btn2.place(x=100, y=305, width=100, height=50)
btn3 = tk.Button(window, text="Влево", bg="green")
btn3.place(x=45, y=250, width=50, height=105)
btn4 = tk.Button(window, text="Вправо", bg="green")
btn4.place(x=205, y=250, width=50, height=105)
btn5 = tk.Button(window, text="Перезапустить игру", bg="green", command=restart)
btn5.place(x=45, y=360, width=210, height=50)
window.mainloop()
