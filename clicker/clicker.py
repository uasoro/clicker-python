from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror, showwarning, showinfo
import keyboard
keyboard = keyboard.add_hotkey

#проверка сохранения
with open('C:\Projects\PROJECTX\main\clicker\click.txt', 'r') as f:
    x = f.readline()
#проверка на правильность сохранения
if x.isdigit() == True:
    a = int(x)
else:
    showerror(title="error", message="Ошибка! Проверьте правильность click.txt и попробуйте снова!")
    exit(0)
    
#создание основного окна
root = tk.Tk()
root.title('Панель')
root.geometry("600x500")
root.configure(bg='Lavender')
root.attributes("-alpha", 0.9)
root.attributes("-toolwindow", True)

main_menu = Menu() #создание верхнего меню

#создание кнопок для полноэкранного режима и выключения
def f11():
    root.attributes("-fullscreen", True)
def esc():
    with open('C:\Projects\PROJECTX\main\clicker\click.txt', 'w+') as f: #сохранение прогресса
        x = f.write(str(a))
    root.destroy()
keyboard('F11', f11) #контроль нажатия кнопки 'F11'
keyboard('Esc', esc) #контроль нажатия кнопки 'Esc'

def setting(): #функции настроек
    #создание окна настроек
    set = tk.Toplevel(root)
    set.title('Settings')
    set.geometry("300x250")
    set.configure(bg='Lavender')
    set.attributes("-toolwindow", True)
    enabled = IntVar()

    def checkbutton_changed(): #функция действия при включении/выключении режима hack
        if enabled.get() == 1:
            main_menu.add_cascade(label="HACK", command=hack) #создание кнопки hack в верхнем меню
            showinfo(title="Info", message="Вы включили режим HACK, теперь его будет видно в верхнем меню")
            set.destroy()
        else:
            showinfo(title="Info", message="Отключено")

    def whatt(): #функция действия при нажатии на кнопку что это
        showinfo(title="Info", message="HACK - специальный режим чтобы хакнуть эту игру")

    enabled_checkbutton = Checkbutton(set, text="HACK", bg='lavender', variable=enabled)
    apply = tk.Button(set, text="APPLY", width=10, height=1, bg = 'skyblue', command=checkbutton_changed)
    what = tk.Button(set, text="Что это?", width=8, height=1, bg = 'gray65', command=whatt)
    enabled_checkbutton.pack(anchor=CENTER)
    what.pack(anchor=CENTER)
    apply.pack(side=BOTTOM, anchor=S)

def hack():
    # создание окна hack
    window = tk.Toplevel(root)
    window.title('HACK')
    window.geometry("300x250")
    window.configure(bg='Lavender')
    window.attributes("-toolwindow", True)
    entry = Entry(window)
    errmsg = StringVar()

    def enter(): #функция режима hack
        global a
        kol = entry.get()
        if kol.isdigit() == True:
            a = int(kol)
            label.config(text=str (a)+'$')
            window.destroy()
        else:
            errmsg.set("Пожалуйста, введите корректное число!")
            error = Label(window, fg="red", bg= 'lavender', textvariable=errmsg, wraplength=250)
            error.pack(padx=5, pady=5, anchor=NW)

    lbl = Label(window, text='Введите новое значение:', background='Lavender', foreground='DarkGreen')
    btnn = tk.Button(window, text="HACK!!!", width=10, height=2, bg = 'skyblue', command=enter)
    lbl.pack()
    entry.pack(expand=1)
    btnn.pack(expand=1)
    window.mainloop()

#добавление кнопки настроек в верхнее меню
main_menu.add_cascade(label="Settings", command=setting)

def reset(): #функция кнопки reset на главном окне
    global a
    showwarning(title="reset", message="Ваш прогресс был полностью сброшен!\nВоспользуйтесь HACK если это было случайно и вы хотите его восстановить.")
    a = 0
    label.config(text=str (a)+'$')

def plus(): #функция основной кнопки Click
    global a
    a = a + 1
    label.config(text=str (a)+'$')

#располагаем reset, click и $ на основном окне
btn2 = tk.Button(text="Reset", command=reset, bg='gray65')
btn2.pack()
label = Label(text=str (a)+'$', font=("Arial", 50), borderwidth=2, background='Lavender', foreground='LimeGreen')
label.pack()
btn = tk.Button(text="Click", command=plus, width=20, height=4, bg='skyblue')
btn.pack()

def on_closing(): #функция сохранения прогресса при закрытии
    with open('C:\Projects\PROJECTX\main\clicker\click.txt', 'w+') as f:
        x = f.write(str(a))
    root.destroy()

root.config(menu=main_menu) 
root.protocol("WM_DELETE_WINDOW", on_closing) #действие при закрытии
root.mainloop()