from tkinter import *
alphabetRU = [["а", "б", "в", "г", "д", "е"],
              ["ё", "ж", "з", "и", "й", "к"],
              ["л", "м", "н", "о", "п", "р"],
              ["с", "т", "у", "ф", "х", "ц"],
              ["ч", "ш", "щ", "ъ", "ы", "ь"],
              ["э", "ю", "я", ".", ",", "!"],
              ["?", ";", ":", "-", "—", "("],
              ["0", "1", "2", "3", "4", "5"],
              ["6", "7", "8", "9", "=", "*"],
              [")", "\"", "'", "«", "»", "+"]]
alphabetEN = [["a", "b", "c", "d", "e"],
              ["f", "g", "h", "i", "j"],
              ["k", "l", "m", "n", "o"],
              ["p", "q", "r", "s", "t"],
              ["u", "v", "w", "x", "y"],
              ["z", ".", ",", "!", "?"],
              [";", ":", "-", "—", "("],
              ["0", "1", "2", "3", "4"],
              ["5", "6", "7", "8", "9"],
              [")", "\"", "'", "«", "»"]]
RU = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
EN = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
root = Tk()
root.configure(bg='#eef2f6')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Шифрование текста методом Шифра Полибия")
frame1 = Frame(root, borderwidth=1, relief=GROOVE, background="white", padx=8, pady=10)
frame1.place(relwidth=0.45, relx=0.04, rely=0.1)
frame2 = Frame(root, borderwidth=1, relief=GROOVE, background="#1e2b3a", padx=8, pady=10)
frame2.place(relwidth=0.45, relx=0.5, rely=0.1)
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-alpha', 0.6)
label = Label(frame1, text="Введите текст для шифрования", padx=8, pady=8, font=("Segoe UI", 14, "bold"), background="white")
label.pack(anchor=W)
label = Label(frame2, text="Результат шифрования", padx=8, pady=8, font=("Segoe UI", 14, "bold"), foreground="#a9c1d9", background="#1e2b3a")
label.pack(anchor=W)
ru = "Русский"
en = "Английский"
frame3 = Frame(frame1, borderwidth=1, relief=GROOVE, background="white", padx=8, pady=10)
frame3.pack(fill=X, pady=5)
frame4 = Frame(frame1, borderwidth=1, relief=GROOVE, background="white", padx=8, pady=10)
frame4.pack(fill=X, pady=5)
lang = StringVar(value=ru)
Label(frame3, text="Выберите язык:", background="white", font=("Segoe UI", 10)).grid(row=0, column=0, columnspan=2, sticky=W, pady=5)
radio_ru = Radiobutton(frame3, text=ru, value=ru, variable=lang, background="white")
radio_ru.grid(row=1, column=0, padx=10, pady=2, sticky=W)
radio_en = Radiobutton(frame3, text=en, value=en, variable=lang, background="white")
radio_en.grid(row=1, column=1, padx=10, pady=2, sticky=W)
num = "Цифры"
ruSign = "Русский алфавит"
enSign = "Английский алфавит"
shifr = StringVar(value=num)
Label(frame4, text="Выберите тип шифрования:", background="white", font=("Segoe UI", 10)).grid(row=0, column=0, columnspan=2, sticky=W, pady=5)
radio_num = Radiobutton(frame4, text="Цифры", value="Цифры", variable=shifr, background="white")
radio_num.grid(row=1, column=0, padx=10, pady=2, sticky=W)
radio_rus = Radiobutton(frame4, text="Русский алфавит", value="Русский алфавит", variable=shifr, background="white")
radio_rus.grid(row=1, column=1, padx=10, pady=2, sticky=W)
radio_en_sign = Radiobutton(frame4, text="Английский алфавит", value="Английский алфавит", variable=shifr, background="white")
radio_en_sign.grid(row=1, column=2, padx=10, pady=2, sticky=W)
txt = Text(frame1)
txt.pack(fill=X, pady=10, padx=5)
chek = Label(frame2, background="#1e2b3a")
chek.pack()
cod_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8,foreground="#a9c1d9", font=("Arial", 14))
cod_text.pack(fill=BOTH, expand=True)
decoded_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8,foreground="#a9c1d9", font=("Arial", 14))
decoded_text.pack(fill=BOTH, expand=True)
def click_button():
    text = txt.get("1.0", "end-1c")
    text = text.lower().replace(" ", "")
    coded = ""

    if lang.get() == "Русский":
        a = alphabetRU
    else:
        a = alphabetEN
    for i in text:
        for j in a:
            if i in j:
                if shifr.get() == "Цифры":
                    coded += str(a.index(j)) + str(j.index(i))
                elif shifr.get() == "Русский алфавит":
                    coded += RU[a.index(j)] + RU[j.index(i)]
                else:
                    coded += EN[a.index(j)] + EN[j.index(i)]
    cod_text.delete("1.0", END)
    cod_text.insert("1.0", coded)
    print(coded)
    t = ""
    for i in range(0, len(coded) - 1, 2):
        if shifr.get() == "Цифры":
            t += a[int(coded[i])][int(coded[i + 1])]
        elif shifr.get() == "Русский алфавит":
            t += a[int(RU.index(coded[i]))][int(RU.index(coded[i+1]))]
        else:
            t += a[int(EN.index(coded[i]))][int(EN.index(coded[i+1]))]
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
btn_encrypt = Button(button_frame, text="Зашифровать", command=click_button, background="#1e2b3a", foreground="white", width=15)
btn_encrypt.pack(side=LEFT, padx=5)
btn_clear = Button(button_frame, text="Очистить", command=clear, background="#1e2b3a", foreground="white", width=15)
btn_clear.pack(side=LEFT, padx=5)
root.mainloop()
