import random
from tkinter import *

root = Tk()
root.configure(bg='#eef2f6')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Шифрование текста методом Шифра Полибия")
frame1 = Frame(root, borderwidth=1, relief=GROOVE, background="white", padx=8, pady=10)
frame1.place(relwidth=0.45, relheight=0.8, relx=0.04, rely=0.1)
frame2 = Frame(root, borderwidth=1, relief=GROOVE, background="#1e2b3a", padx=8, pady=10)
frame2.place(relwidth=0.45, relheight=0.8, relx=0.5, rely=0.1)
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-alpha', 0.6)
label = Label(frame1, text="Введите текст для шифрования", padx=8, pady=8, font=("Segoe UI", 14, "bold"),
              background="white")
label.pack(anchor=W)
label = Label(frame2, text="Результат шифрования", padx=8, pady=8, font=("Segoe UI", 14, "bold"), foreground="#a9c1d9",
              background="#1e2b3a")
label.pack(anchor=W)

txt = Text(frame1)
txt.pack(fill=X, pady=10, padx=5)
label = Label(frame1, text="Исходные байты:", padx=8, pady=8, font=("Segoe UI", 14, "bold"),
              background="white")
label.pack(anchor=W)
text_bytes = Text(frame1, padx=8, pady=8, wrap=WORD, height=8, font=("Arial", 14))
text_bytes.pack(fill=BOTH, expand=True)
chek = Label(frame2, background="#1e2b3a")
chek.pack()
label = Label(frame2, text="Зашифрованные данные:", padx=8, pady=8, font=("Segoe UI", 14, "bold"), foreground="#a9c1d9",
              background="#1e2b3a")
label.pack(anchor=W)
cod_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9",
                font=("Arial", 14))
cod_text.pack(fill=BOTH, expand=True)
label = Label(frame2, text="Расшифровано (данные):", padx=8, pady=8, font=("Segoe UI", 14, "bold"),
              foreground="#a9c1d9",
              background="#1e2b3a")
label.pack(anchor=W)
decoded_text = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9",
                    font=("Arial", 14))
decoded_text.pack(fill=BOTH, expand=True)
label = Label(frame2, text="Расшифровано (байты):", padx=8, pady=8, font=("Segoe UI", 14, "bold"), foreground="#a9c1d9",
              background="#1e2b3a")
label.pack(anchor=W)
decoded_bytes = Text(frame2, padx=8, pady=8, background="#1e2b3a", wrap=WORD, height=8, foreground="#a9c1d9",
                     font=("Arial", 14))
decoded_bytes.pack(fill=BOTH, expand=True)


def click_button():
    key = random.randbytes(64)
    keys_for_round = []
    for i in range(0, len(key), 4):
        keys_for_round.append(key[i:i + 4])
    sBox = [random.sample(range(4), 4) for _ in range(16)]
    sBox = [{i: s[i] for i in range(len(s))} for s in sBox]
    # text = input("Введите текст: ")
    text = txt.get("1.0", "end-1c")
    coded = bytes()
    text = text.encode("utf-8")
    print(f"\t  Исходные байты: {text}")
    text_bytes.delete("1.0", END)
    text_bytes.insert("1.0", text)
    for i in range(0, len(text), 8):
        block = text[i:i + 8]
        if len(block) < 8:
            block = block + b'\x00' * (8 - len(block))
        L, R = block[0:4], block[4:8]
        for j in range(16):
            L_int = int.from_bytes(L, byteorder='big')
            key_int = int.from_bytes(keys_for_round[j], byteorder='big')
            L_int = L_int ^ key_int

            L = L_int.to_bytes(4, byteorder='big')
            L = list(L)
            temp_L = L.copy()
            for k, l in sBox[j].items():
                temp_L[k] = L[l]
            L = temp_L
            L = bytes(L)

            L_int = int.from_bytes(L, byteorder='big')
            R_int = int.from_bytes(R, byteorder='big')
            L_int = L_int ^ R_int
            L = L_int.to_bytes(4, byteorder='big')
            R = R_int.to_bytes(4, byteorder='big')
            if j < 15:
                L, R = R, L
        coded += (L) + (R)

    cod_text.delete("1.0", END)
    cod_text.insert("1.0", coded)
    print(f"Зашифрованные данные: {coded}")
    sBox_revers = [{i: j for j, i in s.items()} for s in sBox]
    decoded = bytes()
    for i in range(0, len(coded), 8):
        block = coded[i:i + 8]
        L, R = block[0:4], block[4:8]
        for j in range(15, -1, -1):
            if j < 15:
                L, R = R, L

            R_int = int.from_bytes(R, byteorder='big')
            L_int = int.from_bytes(L, byteorder='big')
            L_int = L_int ^ R_int
            L = L_int.to_bytes(4, byteorder='big')

            L = list(L)
            temp_L = L.copy()
            for k, l in sBox_revers[j].items():
                temp_L[k] = L[l]
            L = temp_L
            L = bytes(L)

            L_int = int.from_bytes(L, byteorder='big')
            key_int = int.from_bytes(keys_for_round[j], byteorder='big')
            L_int = L_int ^ key_int
            L = L_int.to_bytes(4, byteorder='big')

        decoded += L + R

    decoded = decoded.rstrip(b'\x00')
    decoded_text.delete("1.0", END)
    decoded_text.insert("1.0", decoded.decode("utf-8", errors='ignore'))
    decoded_bytes.delete("1.0", END)
    decoded_bytes.insert("1.0", decoded)
    print(f"Расшифровано (байты): {decoded}")
    print(f"Расшифровано (данные): {decoded.decode("utf-8", errors='ignore')}")
    if decoded == text:
        chek.config(text="Кодирование прошло успешно", background="#ccff99", foreground="#009900", padx=8, pady=8)
    else:
        chek.config(text="Произошли ошибки", background="#FFCDD2", foreground="#B71C1C", padx=8, pady=8)


def clear():
    cod_text.delete("1.0", END)
    chek.config(text="")
    decoded_text.delete("1.0", END)
    decoded_bytes.delete("1.0", END)
    text_bytes.delete("1.0", END)


button_frame = Frame(frame1, background="white")
button_frame.pack(fill=X, pady=5)
btn_encrypt = Button(button_frame, text="Зашифровать", command=click_button, background="#1e2b3a", foreground="white",
                     width=15)
btn_encrypt.pack(side=LEFT, padx=5)
btn_clear = Button(button_frame, text="Очистить", command=clear, background="#1e2b3a", foreground="white", width=15)
btn_clear.pack(side=LEFT, padx=5)
root.mainloop()
