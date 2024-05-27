import tkinter as tk
from random import randint

symbols_list = ['a', 'b', 'c', 'd', 'e', 'f', 'j']


def any40s():
    try:
        word = len(symbols_list) - 1
        result = []
        for i in range(40):
            a = randint(0, word)
            res = symbols_list[a]
            result.append(res)
        return result
    except:
        return "Произошла ошибка!"


def show_result():
    result_list = any40s()
    result_text.delete("1.0", "end")
    result_text.insert("1.0", ''.join(result_list))


root = tk.Tk()
root.title("40 любых символов")

personal_frame = tk.LabelFrame(root, text="40 рандомных символов")
personal_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

result_text = tk.Text(personal_frame, height=3, width=30)
result_text.grid(row=0, column=0)

button = tk.Button(root, text="Сгенерировать", command=show_result)
button.grid(row=1, column=0)

root.mainloop()