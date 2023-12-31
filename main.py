import tkinter as tk
from tkinter import messagebox
from random import randint


game_end = False
win = False
flag = False
size = 4


def size4():
    global size
    size = 4
    restart()


def size5():
    global size
    size = 5
    restart()


def size6():
    global size
    size = 6
    restart()


def end_check(matrix, size):
    for i in range(size-1):
        for j in range(size-1):
            if matrix[i][j] == 0:
                return False
            if matrix[i][j] == matrix[i][j + 1]:
                return False
            if matrix[i][j] == matrix[i + 1][j]:
                return False
    for i in range(size-1):
        if matrix[size-1][i] == 0 or matrix[i][size-1] == 0:
            return False
        if matrix[size-1][i] == matrix[size-1][i + 1]:
            return False
        if matrix[i][size-1] == matrix[i + 1][size-1]:
            return False
    if matrix[size-1][size-1] == 0:
        return False
    return True


def win_check(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 2048:
                return True
    return False


def generate_points():
    global size
    countZeros = 0
    for i in range(size):
        for j in range(size):
            if matrix1[i][j] == 0:
                countZeros += 1
    ZeroNumber = randint(1, countZeros)
    number = 0
    if randint(1, 8) == 8:
        newNumeric = 4
    else:
        newNumeric = 2
    for i in range(size):
        for j in range(size):
            if matrix1[i][j] == 0:
                number += 1
                if number == ZeroNumber:
                    matrix1[i][j] = newNumeric
                    break
        if number == ZeroNumber:
            break


def generate_matrix():
    global size
    matrix: list[list[int]] = [[0 for x in range(size)] for y in range(size)]
    number = randint(1, 100)
    position1 = randint(1, size ** 2)
    position2 = randint(1, size ** 2)
    while position1 == position2:
        position2 = randint(1, size ** 2)
    if number < 80:
        matrix[(position1 - 1) // size][position1 % size - 1] = 2
        matrix[(position2 - 1) // size][position2 % size - 1] = 2
    elif number == 80:
        matrix[(position1 - 1) // size][position1 % size - 1] = 4
        matrix[(position2 - 1) // size][position2 % size - 1] = 4
    else:
        matrix[(position1 - 1) // size][position1 % size - 1] = 2
        matrix[(position2 - 1) // size][position2 % size - 1] = 4
    return matrix


def restart():
    global win
    win = False
    global flag
    flag = False
    global game_end
    game_end = False
    global matrix1
    matrix1 = generate_matrix()
    paint()


def right():
    global matrix1
    global size
    done = False
    i = 0
    while i < size:
        j = size - 2
        afterUnion = False
        while j > -1:
            if j != size - 1 and matrix1[i][j] != 0:
                if matrix1[i][j+1] == 0:
                    done = True
                    matrix1[i][j+1] = matrix1[i][j]
                    matrix1[i][j] = 0
                    j += 2
                elif matrix1[i][j+1] == matrix1[i][j] and not afterUnion:
                    done = True
                    matrix1[i][j+1] *= 2
                    matrix1[i][j] = 0
                    afterUnion = True
                else:
                    afterUnion = False
            j -= 1
        i += 1
    if done:
        generate_points()
    if end_check(matrix1, size):
        global game_end
        game_end = True
    if win_check(matrix1, size):
        global win
        win = True
    paint()


def left():
    global matrix1
    global size
    done = False
    i = 0
    while i < size:
        j = 1
        afterUnion = False
        while j < size:
            if j != 0 and matrix1[i][j] != 0:
                if matrix1[i][j - 1] == 0:
                    done = True
                    matrix1[i][j - 1] = matrix1[i][j]
                    matrix1[i][j] = 0
                    j -= 2
                elif matrix1[i][j - 1] == matrix1[i][j] and not afterUnion:
                    done = True
                    matrix1[i][j - 1] *= 2
                    matrix1[i][j] = 0
                    afterUnion = True
                else:
                    afterUnion = False
            j += 1
        i += 1
    if done:
        generate_points()
    if end_check(matrix1, size):
        global game_end
        game_end = True
    if win_check(matrix1, size):
        global win
        win = True
    paint()


def up():
    global matrix1
    global size
    done = False
    i = 0
    while i < size:
        j = 1
        afterUnion = False
        while j < size:
            if j != 0 and matrix1[j][i] != 0:
                if matrix1[j - 1][i] == 0:
                    done = True
                    matrix1[j - 1][i] = matrix1[j][i]
                    matrix1[j][i] = 0
                    j -= 2
                elif matrix1[j - 1][i] == matrix1[j][i] and not afterUnion:
                    done = True
                    matrix1[j - 1][i] *= 2
                    matrix1[j][i] = 0
                    afterUnion = True
                else:
                    afterUnion = False
            j += 1
        i += 1
    if done:
        generate_points()
    if end_check(matrix1, size):
        global game_end
        game_end = True
    if win_check(matrix1, size):
        global win
        win = True
    paint()


def down():
    global matrix1
    global size
    done = False
    i = 0
    while i < size:
        j = size - 2
        afterUnion = False
        while j > -1:
            if j != size - 1 and matrix1[j][i] != 0:
                if matrix1[j + 1][i] == 0:
                    done = True
                    matrix1[j + 1][i] = matrix1[j][i]
                    matrix1[j][i] = 0
                    j += 2
                elif matrix1[j + 1][i] == matrix1[j][i] and not afterUnion:
                    done = True
                    matrix1[j + 1][i] *= 2
                    matrix1[j][i] = 0
                    afterUnion = True
                else:
                    afterUnion = False
            j -= 1
        i += 1
    if done:
        generate_points()
    if end_check(matrix1, size):
        global game_end
        game_end = True
    if win_check(matrix1, size):
        global win
        win = True
    paint()


def paint():
    global size
    length = 56
    space = 5
    f = 14
    if size == 5:
        length = 45
        space = 4
        f = 12
    elif size == 6:
        length = 38
        space = 3
        f = 10
    canvas.delete("all")
    for i in range(1, size+1):
        for j in range(1, size+1):
            if matrix1[i - 1][j - 1] != 0:
                canvas.create_rectangle(space * j + length * (j - 1), space * i + length * (i - 1),
                                        space * j + length * j, space * i + length * i, fill="white")
                canvas.create_text(space * j + length * (j - 1) + (length-1)//2+1, space * i + length * (i - 1) +
                                   (length-1)//2+1, text=matrix1[i-1][j-1], font=f"calibre {f}", justify="center",
                                   fill="black")
    canvas.pack()
    if game_end:
        messagebox.showinfo("Информация о игре", "Игра окончена")
    global flag
    if win and not flag:
        messagebox.showinfo("Информация о игре", "Вы выиграли")
        flag = True


window = tk.Tk()
window.title("2048")
w = (window.winfo_screenwidth()-300)//2
h = (window.winfo_screenheight()-420)//2
window.geometry(f'300x480+{w}+{h}')
window.resizable(False, False)
matrix1 = generate_matrix()
canvas = tk.Canvas(window, width=249, height=249, bg="gray")
paint()
btn1 = tk.Button(window, text="Вверх", bg="green", command=up)
btn1.place(x=100, y=255, width=100, height=50)
btn2 = tk.Button(window, text="Вниз", bg="green", command=down)
btn2.place(x=100, y=310, width=100, height=50)
btn3 = tk.Button(window, text="Влево", bg="green", command=left)
btn3.place(x=45, y=255, width=50, height=105)
btn4 = tk.Button(window, text="Вправо", bg="green", command=right)
btn4.place(x=205, y=255, width=50, height=105)
btn5 = tk.Button(window, text="Перезапустить игру", bg="green", command=restart)
btn5.place(x=45, y=365, width=210, height=50)
btn6 = tk.Button(window, text="4x4", bg="green", command=size4)
btn6.place(x=45, y=420, width=66, height=50)
btn7 = tk.Button(window, text="5x5", bg="green", command=size5)
btn7.place(x=117, y=420, width=66, height=50)
btn8 = tk.Button(window, text="6x6", bg="green", command=size6)
btn8.place(x=189, y=420, width=66, height=50)
window.mainloop()
