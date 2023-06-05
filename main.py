from tkinter import *
from secrets import choice
import string


def generate_password() -> None:
    """
    Основная функция, генерирует пароль основываясь на 1 slider, 2 radiobuttons и 4 checkbuttons
    :return: Выводит результат генерации на GUI по нажатию кнопки generate_password_button
    """
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + \
                      checkbutton_symbols_var.get()
    if radiobutton_var.get() == 0:
        character_list = get_easy_to_read_tableset(checkbutton_sum)
    elif radiobutton_var.get() == 1:
        character_list = get_easy_to_say_tableset(checkbutton_sum)
    password = []
    for symbol in range(pass_len.get()):
        password.append(choice(character_list))
    password = ''.join(password)
    password_text.set(password)


def get_easy_to_read_tableset(value: int) -> str:
    """
    Создает кастомный набор легкоразлечимых символов
    :param value: Сумма 4 checkbuttons для получения всех комбинаций
    :return: Одна из 15 комбинаций символов для генерации пароля
    """
    character_list = ''
    upper = 'ABCDEFGHJKMNPQRSTUVXYZ'
    lower = 'abcdefghjkmnpqrstuvxyz'
    numbers = '23456789'
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\]_{}~'
    match value:
        case 1:
            character_list = upper
        case 10:
            character_list = lower
        case 11:
            character_list = upper+lower
        case 100:
            character_list = numbers
        case 101:
            character_list = upper+numbers
        case 110:
            character_list = lower+numbers
        case 111:
            character_list = upper+lower+numbers
        case 1_000:
            character_list = symbols
        case 1_001:
            character_list = upper+symbols
        case 1_010:
            character_list = lower+symbols
        case 1_011:
            character_list = upper+lower+symbols
        case 1_100:
            character_list = numbers+symbols
        case 1_101:
            character_list = upper+numbers+symbols
        case 1_110:
            character_list = lower+numbers+symbols
        case 1_111:
            character_list = upper+lower+numbers+symbols
    return character_list


def get_easy_to_say_tableset(value: int) -> str:
    """
    Создает набор из заглавных и строчных букв
    :param value: Сумма 2 checkbuttons для получения всех комбинаций
    :return: Одна из 3 комбинаций символов для генерации пароля
    """
    character_list = ''
    if value == 1:
        character_list += string.ascii_uppercase
    elif value == 10:
        character_list += string.ascii_lowercase
    elif value == 11:
        character_list += string.ascii_letters
    return character_list


# Скрипты элементов tkinter
def check_whether_password_len_is_valid(event=None) -> None:
    """
    Проверяет длину пароля в Entry и не позволяет сделать его вне установленного диапазона
    """
    try:
        int(password_length_entry.get())
        if int(password_length_entry.get()) < 4:
            pass_len_txt.set('4')
            pass_len.set(4)
        elif int(password_length_entry.get()) > 20:
            pass_len_txt.set('20')
            pass_len.set(20)
    except ValueError:
        pass_len_txt.set('4')


def change_entry_len_to_match_slider(event=None) -> None:
    """
    Изменяет значение в Entry на значение выбранное в Slider
    """
    password_length_entry.delete(0, END)
    password_length_entry.insert(0, pass_len.get())


def activate_checkboxes_on_radiobutton() -> None:
    """
    Делает активными 2 checkbox при нажании кнопки 'Easy to read'
    """
    checkbutton_numbers.config(state='active')
    checkbutton_numbers_var.set(100)
    checkbutton_symbols.config(state='active')
    checkbutton_symbols_var.set(1_000)


def disable_checkboxes_on_radiobutton() -> None:
    """
    Делает неактивными 2 чекбокса при нажатии кнопки 'Easy to say'
    """
    checkbutton_numbers.config(state='disabled')
    checkbutton_numbers_var.set(0)
    checkbutton_symbols.config(state='disabled')
    checkbutton_symbols_var.set(0)
    checkbutton_upper_var.set(1)


def make_1_checkbutton_active(checkbutton: object) -> None:
    """
    Проверяет состояние четырех checkbox и если остался только один, не даёт его выключить
    """
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() +\
                      checkbutton_symbols_var.get()
    if checkbutton_sum == 0:
        match str(checkbutton):
            case 'PY_VAR3': checkbutton.set(1)
            case 'PY_VAR4': checkbutton.set(10)
            case 'PY_VAR5': checkbutton.set(100)
            case 'PY_VAR6': checkbutton.set(1_000)


def copy_on_button(event=None) -> None:
    """
    Копирует значение Label 'generated_password' по нажатию кнопки 'Copy'
    """
    window.clipboard_clear()
    window.clipboard_append(password_text.get())


# Tk initialization
window = Tk()
window.title('Password Generator')
window.geometry('330x310+100+100')

# Vars
pass_len = IntVar(value=10)
pass_len_txt = StringVar(value=10)
radiobutton_var = IntVar()
checkbutton_upper_var = IntVar(value=1)
checkbutton_lower_var = IntVar(value=10)
checkbutton_numbers_var = IntVar(value=100)
checkbutton_symbols_var = IntVar(value=1_000)
password_text = StringVar()
password_text.set('Your password will be here')

# Frames
window.configure(background='#141414', cursor='left_ptr')
length_frame = Frame(master=window, background='#141414', pady=8)
length_subframe_1 = Frame(master=length_frame)
length_subframe_2 = Frame(master=length_frame)
radiobutton_frame = Frame(master=window, background='#141414')
checkbutton_frame = Frame(master=window, background='#141414')
checkbutton_subframe_1 = Frame(master=checkbutton_frame, background='#141414', border=5)
checkbutton_subframe_2 = Frame(master=checkbutton_frame, background='#141414', border=5)
password_frame = Frame(master=window, background='#141414', border=5)

length_label = Label(master=length_frame, text='Password Length', font='Verdana 11 bold', fg='#141414', bg='#0C7489',
                     bd=3, padx=80, relief=FLAT)
password_length_entry = Entry(master=length_subframe_1, textvariable=pass_len_txt, width=13, font='Verdana',
                              justify=CENTER, background='#119DA4', bd=0, relief=FLAT, cursor='arrow',
                              selectborderwidth=0, selectforeground='#141414', selectbackground='white')
password_length_scale = Scale(master=length_subframe_2, from_=4, to=20, variable=pass_len, length=130,
                              highlightthickness=0, orient='horizontal', sliderlength=15, font='Verdana', fg='#141414',
                              background='#119DA4', bd=0, relief=FLAT, sliderrelief=GROOVE, troughcolor='#BAEBEE',
                              cursor='arrow')

radiobutton_easy_to_read = Radiobutton(master=radiobutton_frame, text='Easy to read', variable=radiobutton_var,
                                       value=0, command=activate_checkboxes_on_radiobutton, font='Verdana',
                                       fg='#141414', activeforeground='white', bg='#0C7489',
                                       activebackground='#119DA4', borderwidth=4, cursor='arrow')
radiobutton_easy_to_say = Radiobutton(master=radiobutton_frame, text='Easy to say', variable=radiobutton_var,
                                      value=1, command=disable_checkboxes_on_radiobutton, font='Verdana',
                                      fg='#141414', activeforeground='white', bg='#119DA4', activebackground='#119DA4',
                                      borderwidth=4, background='#0C7489', cursor='arrow')

checkbutton_upper = Checkbutton(master=checkbutton_subframe_1, text='Uppercase', variable=checkbutton_upper_var,
                                command=lambda: make_1_checkbutton_active(checkbutton_upper_var), font='Verdana',
                                fg='#141414', activeforeground='white', bg='#119DA4', activebackground='#119DA4',
                                borderwidth=4, background='#0C7489', cursor='arrow')
checkbutton_lower = Checkbutton(master=checkbutton_subframe_1, text='Lowercase', variable=checkbutton_lower_var,
                                onvalue=10, command=lambda: make_1_checkbutton_active(checkbutton_lower_var),
                                font='Verdana', fg='#141414', activeforeground='white', bg='#119DA4',
                                activebackground='#119DA4', borderwidth=4, background='#0C7489', cursor='arrow')
checkbutton_numbers = Checkbutton(master=checkbutton_subframe_2, text='Numbers', variable=checkbutton_numbers_var,
                                  onvalue=100, command=lambda: make_1_checkbutton_active(checkbutton_numbers_var),
                                  font='Verdana', fg='#141414', activeforeground='white', bg='#119DA4',
                                  activebackground='#119DA4', borderwidth=4, background='#0C7489', cursor='arrow')
checkbutton_symbols = Checkbutton(master=checkbutton_subframe_2, text='Symbols', variable=checkbutton_symbols_var,
                                  onvalue=1_000, command=lambda: make_1_checkbutton_active(checkbutton_symbols_var),
                                  font='Verdana', justify=LEFT, padx=3, fg='#141414', activeforeground='white',
                                  bg='#119DA4', activebackground='#119DA4', borderwidth=4, background='#0C7489',
                                  cursor='arrow')

generated_password = Label(master=password_frame, textvariable=password_text, font='Verdana 13 bold', width=24, pady=4,
                           fg='#141414', bg='#BAEBEE', bd=4, relief=FLAT, highlightthickness=0,
                           highlightbackground='#141414')
generate_password_button = Button(master=password_frame, text='Generate', command=generate_password, font='Verdana',
                                  width=11, fg='#141414', bg='#0C7489', activebackground='#119DA4',
                                  activeforeground='white', bd=1, relief=FLAT)
copy_generated_password = Button(master=password_frame, text='Copy', font='Verdana', width=10, fg='#141414',
                                 bg='#0C7489', activebackground='#119DA4', activeforeground='white', bd=1, relief=FLAT)

# Binds
password_length_entry.bind('<KeyRelease>', check_whether_password_len_is_valid)
password_length_scale.bind('<ButtonRelease-1>', change_entry_len_to_match_slider)
copy_generated_password.bind('<ButtonRelease-1>', copy_on_button)

# Packing
length_frame.pack()
radiobutton_frame.pack(pady=(7, 5))
checkbutton_frame.pack(pady=(0, 5))
checkbutton_subframe_1.pack(side=LEFT)
checkbutton_subframe_2.pack()
password_frame.pack()
length_label.pack()
length_subframe_1.pack(side=LEFT, padx=(16, 8),pady=(8, 0), anchor='n')
length_subframe_2.pack(pady=(8, 0))
password_length_entry.pack()
password_length_scale.pack()
radiobutton_easy_to_read.pack(side=LEFT, padx=(4, 12))
radiobutton_easy_to_say.pack(side=RIGHT, padx=0)
checkbutton_upper.pack(pady=5)
checkbutton_lower.pack()
checkbutton_numbers.pack(pady=5)
checkbutton_symbols.pack()
generated_password.pack(pady=(0, 4))
generate_password_button.pack(side=LEFT, padx=(30, 0))
copy_generated_password.pack(anchor='e', padx=(0, 30))


if __name__ == '__main__':
    window.mainloop()
else:
    raise ImportError('Can\'t import this module')
