from main import get_reply
from tkinter import *


def calculate():
    global open_frame
    if open_frame:
        canvas.delete(open_frame)

    positive = list(entry1.get("1.0", END).split())
    negative = list(entry2.get("1.0", END).split())
    reply = get_reply(positive, negative)

    if "Увы, слова " in reply or reply == "Введите хоть что-то!":
        label3 = Label(root, text=f'{reply}', font=('arial', 14))
    else:
        label3 = Label(root, text=f'Итог: {reply}', font=('arial', 14))

    open_frame = canvas.create_window(300, 260, window=label3)


if __name__ == '__main__':

    root = Tk()
    open_frame = None

    canvas = Canvas(root, width=600, height=400, relief='raised')
    canvas.pack()

    label0 = Label(root, text='Косинусное расстояние - это весело!')
    label0.config(font=('arial', 16))
    canvas.create_window(300, 50, window=label0)

    label1 = Label(root, text='Слова, которые нужно включить: ')
    label1.config(font=('arial', 12))
    canvas.create_window(150, 150, window=label1)
    entry1 = Text(root, font=('arial', 10), borderwidth=3, relief=SUNKEN)
    canvas.create_window(150, 200, height=50, width=250, window=entry1)

    label2 = Label(root, text='Слова, которые нужно исключить: ')
    label2.config(font=('arial', 12))
    canvas.create_window(450, 150, window=label2)
    entry2 = Text(root, font=('arial', 10), borderwidth=3, relief=SUNKEN)
    canvas.create_window(450, 200, height=50, width=250, window=entry2)

    button = Button(text='Найти ближайшее слово', command=calculate, height=1, width=25, bg='Salmon1', fg='white',
                    font=('arial', 12, 'bold'))
    canvas.create_window(300, 320, window=button)

    root.mainloop()
