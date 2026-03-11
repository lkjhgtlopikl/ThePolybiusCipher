from click import open_file

import keyGenerate

from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror

root = Tk()
root.configure(bg='#eef2f6')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Шифрование текста методом RSA")
frame1 = Frame(root, borderwidth=1, relief=GROOVE, background="white", padx=8, pady=10)
frame1.place(relwidth=0.45, relheight=0.8, relx=0.04, rely=0.1)
frame2 = Frame(root, borderwidth=1, relief=GROOVE, background="#1e2b3a", padx=8, pady=10)
frame2.place(relwidth=0.45, relheight=0.8, relx=0.5, rely=0.1)
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-alpha', 0.6)
chek = Label(frame2, background="#1e2b3a")
chek.pack()
label = Label(frame1, text="Исходный текст для шифрования", padx=8, pady=8,
              background="white")
label.pack(anchor=W)
txt = Text(frame1)
txt.pack(fill=X, pady=10, padx=5)
label = Label(frame1, text="Коды символов исходного текста в Unicode:", padx=8, pady=8,
              background="white")
label.pack(anchor=W)
text_Unicode = Text(frame1, padx=8, pady=8, wrap=WORD, height=8)
text_Unicode.pack(fill=BOTH, expand=True)
cod_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9")
cod_text.pack(fill=BOTH, expand=True)
decoded_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9")
decoded_text.pack(fill=BOTH, expand=True)
inp = "i"


def open_file():
    global inp
    inp = filedialog.askopenfilename()
    while inp == "":
        showerror(title="Файл не выбран!", message="Выберите файл для шифрования")
        inp = filedialog.askopenfilename()


def click_button():
    with open(inp, 'r', encoding='utf-8') as file:
        text = file.read()
    txt.delete("1.0", END)
    txt.insert("1.0", text)
    textChars = [ord(i) for i in text]
    print(f"textChars = {textChars}")
    text_Unicode.delete("1.0", END)
    text_Unicode.insert("1.0", text)
    e, d, N = keyGenerate.e, keyGenerate.d, keyGenerate.N
    code = [pow(i, e, N) for i in textChars]  # text^e%N
    cod_text.delete("1.0", END)
    cod_text.insert("1.0", code)
    print(f"code = {code}")
    decode = [pow(i, d, N) for i in code]  # code^d%N
    print(f"decode = {decode}")
    result = ""
    for i in decode:
        result += chr(i)
    print(result)
    decoded_text.delete("1.0", END)
    decoded_text.insert("1.0", result)
    file = open("result.txt", "w")
    file.write("Закодировано: " + str(code))
    file.write("\n\nРаскодировано: " + str(decode))
    if result == text:
        chek.config(text="Кодирование прошло успешно", background="#ccff99", foreground="#009900", padx=8, pady=8)
        file.write("\n\nКодирование прошло успешно")
    else:
        chek.config(text="Произошли ошибки", background="#FFCDD2", foreground="#B71C1C", padx=8, pady=8)
        file.write("\n\nПроизошли ошибки")
    file.close()


def clear():
    cod_text.delete("1.0", END)
    chek.config(text="")
    decoded_text.delete("1.0", END)


btn_open = Button(root, text="Открыть файл", command=open_file, background="#1e2b3a", foreground="white", width=15)
btn_open.place(relx=0.025, rely=0.01)
btn_encrypt = Button(frame2, text="Зашифровать", command=click_button, background="white", foreground="#1e2b3a",
                     width=15)
btn_encrypt.pack(side=LEFT, padx=5, pady=5)
btn_clear = Button(frame2, text="Очистить", command=clear, background="white", foreground="#1e2b3a", width=15)
btn_clear.pack(side=RIGHT, padx=5, pady=5)
root.mainloop()
