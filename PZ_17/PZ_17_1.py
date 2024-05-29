import tkinter as tk

root = tk.Tk()
root.title("Персональная информация")

text_info = tk.Label(root, text='Форма заявки на работу в зоопарке')
text_info.config(font=("Courier", 17))
text_info.grid(row=0,column=0)
text_sub_info = tk.Label(root, text='Пожалуйста, заполните форму. Обязательные поля помечены *')
text_sub_info.config(font=("Courier", 8))
text_sub_info.grid(row=1,column=0)
personal_frame = tk.LabelFrame(root, text="Персональная информация")
personal_frame.grid(row=2, column=0, padx=7, pady=7, sticky="nsew")
contact_frame = tk.LabelFrame(root, text="Контактная информация")
contact_frame.grid(row=3, column=0, padx=7, pady=7, sticky="nsew")
preferences_frame = tk.LabelFrame(root, text="Выберите ваших любимых животных:")
preferences_frame.grid(row=4, column=0, padx=7, pady=7, sticky="nsew")


name_label = tk.Label(personal_frame, text="Имя *")
name_label.grid(row=0, column=0, padx=7, pady=7)
name_entry = tk.Entry(personal_frame)
name_entry.grid(row=0, column=1, padx=7, pady=7)

age_label = tk.Label(personal_frame, text="Телефон")
age_label.grid(row=1, column=0, padx=7, pady=7)
age_entry = tk.Entry(personal_frame)
age_entry.grid(row=1, column=1, padx=7, pady=7)

email_label = tk.Label(personal_frame, text="Email *")
email_label.grid(row=2, column=0, padx=7, pady=7)
email_entry = tk.Entry(personal_frame)
email_entry.grid(row=2, column=1, padx=7, pady=7)



phone_label = tk.Label(contact_frame, text="Возврат *")
phone_label.grid(row=0, column=0, padx=7, pady=7, sticky="w")
phone_entry = tk.Entry(contact_frame)
phone_entry.grid(row=0, column=1, padx=7, pady=7, sticky="w")

gender_label = tk.Label(contact_frame, text="Пол")
gender_label.grid(row=1, column=0, padx=7, pady=7, sticky="w")

gender_options = "Мужской"
gender_options1 = "Женский"
gender_var = tk.StringVar()
gender_menu = tk.OptionMenu(contact_frame, gender_var, gender_options, gender_options1)
gender_menu.grid(row=1, column=1)

phone_label1 = tk.Label(contact_frame, text="Перечислите")
phone_label1.grid(row=2, column=0, padx=7, pady=7, sticky="nw")
phone_label2 = tk.Label(contact_frame, text="личные")
phone_label2.grid(row=2, column=0, padx=7, pady=7, sticky="w")
phone_label3 = tk.Label(contact_frame, text="качества")
phone_label3.grid(row=2, column=0, padx=7, pady=7, sticky="sw")
phone_entry = tk.Text(contact_frame, height=4, width=18)
phone_entry.grid(row=2, column=1, padx=7, pady=7)

animals_frame = tk.Frame(preferences_frame)
animals_frame.grid(row=0, column=0)
zeb_check = tk.Checkbutton(animals_frame, text="Зебра")
slon_check = tk.Checkbutton(animals_frame, text="Слон")
cat_check = tk.Checkbutton(animals_frame, text="Кошак")
anti_check = tk.Checkbutton(animals_frame, text="Антилопа")
anak_check = tk.Checkbutton(animals_frame, text="Анаконда")
bird_check = tk.Checkbutton(animals_frame, text="Голубь")
hum_check = tk.Checkbutton(animals_frame, text="Человек")
crab_check = tk.Checkbutton(animals_frame, text="Краб")

zeb_check.grid(row=0, column=0)
slon_check.grid(row=1, column=0)
cat_check.grid(row=0, column=1)
anti_check.grid(row=1, column=1)
anak_check.grid(row=0, column=2)
bird_check.grid(row=1, column=2)
hum_check.grid(row=0, column=3)
crab_check.grid(row=1, column=3)


submit_button = tk.Button(root, text="Отправить информацию")
submit_button.grid(row=5, column=0, pady=1, sticky='w')

root.mainloop()