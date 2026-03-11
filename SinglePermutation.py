import random
from tkinter import *

root = Tk()
root.configure(bg='#eef2f6')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Шифрование текста методом Одиночной перестановки")
frame1 = Frame(root, borderwidth=1, relief=GROOVE, background="white", padx=8, pady=10)
frame1.place(relwidth=0.45, relheight=0.6, relx=0.04, rely=0.1)
frame2 = Frame(root, borderwidth=1, relief=GROOVE, background="#1e2b3a", padx=8, pady=10)
frame2.place(relwidth=0.45, relx=0.5, relheight=0.6, rely=0.1)
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-alpha', 0.6)
label = Label(frame1, text="Введите текст для шифрования", padx=8, pady=8, background="white")
label.pack(anchor=W)
label = Label(frame2, text="Результат шифрования", padx=8, pady=8, foreground="#a9c1d9", background="#1e2b3a")
label.pack(anchor=W)
txt = Text(frame1)
txt.pack(fill=X, pady=10, padx=5)
chek = Label(frame2, background="#1e2b3a")
chek.pack()
cod_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9")
cod_text.pack(fill=BOTH, expand=True)
decoded_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9")
decoded_text.pack(fill=BOTH, expand=True)


def click_button():
    text = txt.get("1.0", "end-1c")
    print(len(text))
    n = 0
    while n == 0:
        for i in range(10, 3, -1):
            if len(text) % i == 0:
                n = i
                break
        if n == 0:
            text += " "
            print(len(text))
    key = random.sample(range(0, n), n)
    key = {i: key[i] for i in range(n)}
    coded = ""
    print(key)
    for i in range(0, len(text), n):
        part = text[i:i + n]
        temp = ''
        for i, j in key.items():
            temp += part[j]
        coded += temp
    cod_text.delete("1.0", END)
    cod_text.insert("1.0", coded)
    print(coded)
    t = ""
    r_key = {i: j for j, i in key.items()}
    for i in range(0, len(coded), n):
        part = coded[i:i + n]
        temp = [""] * n
        for i, j in r_key.items():
            temp[i] = part[j]
        t += ''.join(temp)
    decoded_text.delete("1.0", END)
    decoded_text.insert("1.0", t)
    print(t)
    if t == text:
        chek.config(text="Кодирование прошло успешно", background="#ccff99", foreground="#009900", padx=8, pady=8)
    else:
        chek.config(text="Произошли ошибки", background="#FFCDD2", foreground="#B71C1C", padx=8, pady=8)


def clear():
    cod_text.delete("1.0", END)
    chek.config(text="")
    decoded_text.delete("1.0", END)


button_frame = Frame(frame1, background="white")
button_frame.pack(fill=X, pady=5)
btn_encrypt = Button(button_frame, text="Зашифровать", command=click_button, background="#1e2b3a", foreground="white",
                     width=15)
btn_encrypt.pack(side=LEFT, padx=5)
btn_clear = Button(button_frame, text="Очистить", command=clear, background="#1e2b3a", foreground="white", width=15)
btn_clear.pack(side=LEFT, padx=5)
root.mainloop()
