from tkinter import *
from tkinter import messagebox
import random
import webbrowser
import string

# ISSUES / FEATURES TO ADD
# require tag to save / check if tag exists
# create backup when deleting

password_list_location = 'INSERT APPROPIATE LOCATION FOR THE PASSWORD LIST FILE'


def submit():
    global char_list
    global gen_pass
    gen_pass_list = []
    n = entry_n.get()
    password.delete(0, END)

    if num.get() or alpha.get() or special.get():
        check_any = True
    else:
        check_any = False

    if n.isdigit() and int(n) > 0 and len(str(n)) <= 3 and check_any:
        if num.get():
            for i in string.digits:
                if i not in char_list:
                    char_list.append(i)
        else:
            try:
                for i in string.digits:
                    char_list.remove(i)
            except ValueError:
                None
        if alpha.get():
            for j in string.ascii_letters:
                if j not in char_list:
                    char_list.append(j)
        else:
            try:
                for j in string.ascii_letters:
                    char_list.remove(j)
            except ValueError:
                None
        if special.get():
            for k_0 in range(33, 48):
                if chr(k_0) not in char_list:
                    char_list.append(chr(k_0))
            for k_1 in range(58, 64):
                if chr(k_1) not in char_list:
                    char_list.append(chr(k_1))
            for k_2 in range(91, 97):
                if chr(k_2) not in char_list:
                    char_list.append(chr(k_2))
            for k_3 in range(123, 127):
                if chr(k_3) not in char_list:
                    char_list.append(chr(k_3))
        else:
            try:
                for k_0 in range(33, 48):
                    char_list.remove(chr(k_0))
                for k_1 in range(58, 64):
                    char_list.remove(chr(k_1))
                for k_2 in range(91, 97):
                    char_list.remove(chr(k_2))
                for k_3 in range(123, 127):
                    char_list.remove(chr(k_3))
            except ValueError:
                None

        for i in range(int(n)):
            gen_pass_list += random.choice(char_list)
        gen_pass = "".join(i for i in gen_pass_list)

        password.insert(0, gen_pass)
        gen_pass.replace(gen_pass, "")
    else:
        messagebox.showinfo(title='Error - incorrect input',
                            message='Make sure to :\n- insert correct number of characters (max 3 digit number)\n'
                                    '- check at least one box of what the password should contain',
                            icon='warning')


def clear():
    password.delete(0, END)


def copy():
    window.clipboard_clear()
    window.clipboard_append(password.get())


def save():
    if entry_tag.get() != "":
        text = entry_tag.get() + ": " + password.get() + "\n"
    else:
        text = password.get() + "\n"
    with open(password_list_location, "a") as file:
        if entry_n.get().isdigit() and password.get() != "" and text != "\n":
            file.write(text)


def openfile():
    webbrowser.open(password_list_location)


def delete():
    msgbox = messagebox.askyesno(title='WARNING!',
                                 message='Are you sure you want to delete all saved passwords?',
                                 icon='warning')
    if msgbox:
        with open(password_list_location, "w") as file:
            file.write("")


char_list = []
gen_pass = []

window = Tk()
window.title("Password generator")
window.geometry("300x265")
label_n = Label(window, text="Number of characters:")
label_n.place(x=10, y=10)

entry_n = Entry(window)
entry_n.insert(0, "")
entry_n.place(x=150, y=10)

label_cont = Label(window, text="Password should contain:")
label_cont.place(x=10, y=50)

num = BooleanVar()
check_num = Checkbutton(window,
                        text="Numbers",
                        variable=num,
                        onvalue=True,
                        offvalue=False)
check_num.place(x=10, y=70)

alpha = BooleanVar()
check_alpha = Checkbutton(window,
                          text="Letters",
                          variable=alpha,
                          onvalue=True,
                          offvalue=False)
check_alpha.place(x=100, y=70)

special = BooleanVar()
check_special = Checkbutton(window,
                            text="Special chars",
                            variable=special,
                            onvalue=True,
                            offvalue=False)
check_special.place(x=170, y=70)


butt_submit = Button(window,
                     text="Generate",
                     width=10,
                     command=submit)
butt_submit.place(x=20, y=110)

butt_clear = Button(window,
                    text="Clear",
                    width=10,
                    command=clear)
butt_clear.place(x=110, y=110)

butt_copy = Button(window,
                   text="Copy",
                   width=10,
                   command=copy)
butt_copy.place(x=200, y=110)


password = Entry(window)
password.place(x=91, y=145)

label_line = Label(window, text="___________________________________________________________")
label_line.place(x=0, y=165)

label_tag = Label(window, text="Tag:")
label_tag.place(x=10, y=195)

entry_tag = Entry(window)
entry_tag.insert(0, "")
entry_tag.place(x=50, y=195)

butt_save = Button(window,
                   text="Save",
                   width=10,
                   command=save)
butt_save.place(x=200, y=190)

butt_open = Button(window,
                   text="Open file",
                   width=10,
                   command=openfile)
butt_open.place(x=200, y=225)

butt_del = Button(window,
                  text="Delete file",
                  width=10,
                  command=delete)
butt_del.place(x=110, y=225)

window.mainloop()
