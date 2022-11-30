from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime, date
import requests
import pandas as pd


def set_image():
    global img_base
    with open('savestate_n.txt') as file:
        n = file.read().count(str(1))
    if n < 10:
        path_n = 'n0' + str(n) + '.png'
    else:
        path_n = 'n' + str(n) + '.png'

    path_img = f'{path_main}\\images\\' + path_n
    img_base = PhotoImage(file=path_img)
    label_img = Label(tab1, image=img_base)
    label_img.grid(row=5, column=0, columnspan=8)


def check_n():
    count = -1
    with open('savestate_n.txt') as file:
        n = file.read().count(str(1))
    for i in list_x:
        count += 1
        with open('savestate_n.txt') as file:
            i.set(int(file.read()[count]))
    all_peak_inf.config(text=str(n)+'/28')


def check_peak_height():
    count = -1
    height_list = []
    conq_height = []
    for i in name_list:
        count += 1
        if count < 14:
            height_list.append(int(i[-5:-1]))
        else:
            height_list.append(int(i[-4:-1]))
    with open('savestate_n.txt') as file:
        count = -1
        for i in file.read():
            count += 1
            if i == '1':
                conq_height.append(height_list[count])
    try:
        for i in name_list:
            if str(max(conq_height)) in i:
                temp = i[-5:-1]
                if temp.isdigit():
                    high_peak_inf.config(text=f'{i[0:-6]}, {temp} m')
                else:
                    high_peak_inf.config(text=f'{i[0:-5]}, {temp[1:]} m')
    except ValueError:
        high_peak_inf.config(text='')


def check_last_peak():
    global last_peak_inf
    with open('savestate_date.txt', 'r') as file:
        line_x = file.readlines()
        max_y = 0
        max_m = 0
        max_d = 0
        count = -1
        line_n_list = []
        for i in line_x:
            count += 1
            if 'nieznana' not in i:
                with open('savestate_n.txt') as file2:
                    if file2.read()[count] == '1':
                        temp = i.split('/')
                        temp[2] = temp[2][0:-1]
                        if int(temp[2]) > max_y:
                            max_m = 0
                            max_d = 0
                            line_n_list.clear()
                        if int(temp[2]) >= max_y:
                            max_y = int(temp[2])
                            if int(temp[0]) > max_m:
                                line_n_list.clear()
                            if int(temp[0]) >= max_m:
                                max_m = int(temp[0])
                                if int(temp[1]) > max_d:
                                    line_n_list.clear()
                                if int(temp[1]) >= max_d:
                                    max_d = int(temp[1])
                                    line_n_list.append(count)

    if len(str(max_d)) == 1:
        max_d = '0' + str(max_d)
    if len(str(max_m)) == 1:
        max_m = '0' + str(max_m)
    if len(str(max_y)) == 1:
        max_y = '0' + str(max_y)

    with open('data.txt', 'r') as file:
        line_x = file.readlines()
        name_g = ''
        for i in range(0, len(line_n_list)):
            if line_n_list[i] >= 15:
                name_g += (line_x[line_n_list[i]][0:-5]) + ', '
            else:
                name_g += (line_x[line_n_list[i]][0:-6]) + ', '
            if i == len(line_n_list) - 1:
                name_g = name_g[0:-2]
        if len(line_n_list) > 1:
            last_peak.config(text='Ostatnie zdobyte szczyty: ')
        else:
            last_peak.config(text='Ostatni zdobyty szczyt: ')

    date_output = f'{name_g}, {max_d}.{max_m}.20{max_y}'
    if len(line_n_list) != 0:
        last_peak_inf.config(text=date_output)
    else:
        last_peak_inf.config(text='')


def save():
    list_var = [x0.get(), x1.get(), x2.get(), x3.get(), x4.get(), x5.get(), x6.get(), x7.get(), x8.get(), x9.get(),
                x10.get(), x11.get(), x12.get(), x13.get(), x14.get(), x15.get(), x16.get(), x17.get(), x18.get(),
                x19.get(), x20.get(), x21.get(), x22.get(), x23.get(), x24.get(), x25.get(), x26.get(), x27.get()]
    with open('savestate_n.txt', 'w') as file:
        for i in list_var:
            file.write(str(i))


def boot():
    check_n()
    check_peak_height()
    check_last_peak()
    set_image()


def check_peak():
    save()
    boot()
    try:
        check_date()
    except NameError:
        None
    check_last_peak()


def display(self):
    global i_displayed
    g_name.config(text=gora.get(), font=('Arial', 15, 'bold'))
    with open(f'{path_main}\\data.txt') as file:
        for i, line in enumerate(file):
            if gora.get() in line:
                i_displayed = i
                if i <= 13:
                    g_height.config(text=f'Wysokosc: {line[-5:-1]} m')
                else:
                    g_height.config(text=f'Wysokosc: {line[-4:-1]} m')
                g_check = Checkbutton(tab3, text='Szczyt zdobyty?', variable=list_x[i], bg='white', command=check_peak)
                # g_check.grid(row=2, column=1, sticky=E, padx=20, pady=10)
                g_check.place(x=225, y=85)
                # g_check.place(x=200, y=170)
                check_date()

    g_date.grid(row=4, column=0, sticky=W, padx=20, pady=10)
    # g_date_add.grid(row=4, column=1, sticky=W, padx=20, pady=10)
    g_date_add.place(x=230, y=170)
    # g_date_add.place(x=350, y=170)
    # separator2 = ttk.Separator(tab3, orient='horizontal')
    # separator2.place(x=0, y=208, relwidth=1)

    g_travel.grid(row=5, column=0, sticky=W, padx=20, pady=10)
    g_distance.config(text='check api')
    g_distance.grid(row=5, column=1, sticky=W, padx=20, pady=10)
    # g_time = Label(tab3, text='time', bg='white')
    g_time.grid(row=5, column=3, sticky=W, padx=20, pady=10)
    api_check()


df = pd.read_csv('items.csv')


def api_check():
    key = 'INSERT YOUR GOOGLE API KEY'
    origin = 'INSERT YOUR STARTING LOCATION CITY, POSTAL CODE'
    destination = gora.get()
    df_row = df.query('name == @destination')
    destination_api = df_row.name.values[0] + ' ' + df_row.range.values[0]

    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' \
          f'{origin}&destinations={destination_api}&key={key}'

    response = requests.get(url)
    data = response.json()
    distance = data['rows'][0]['elements'][0]['distance']['text']
    time = data['rows'][0]['elements'][0]['duration']['text']

    g_distance.config(text=distance)
    g_time.config(text=time)


def check_date():
    if list_x[i_displayed].get() == 0:
        g_date.config(text='Data zdobycia: niezdobyta')
        g_date_add.config(text='Dodaj date')
        g_date_add.config(state=DISABLED)
    else:
        with open('savestate_date.txt', 'r') as file:
            line_x = file.readlines()
            date_list = line_x[i_displayed].split('/')

            g_date_add.config(state=NORMAL)
            if 'nieznana' in line_x[i_displayed]:
                g_date_add.config(text='Dodaj date')
                g_date.config(text='Data zdobycia: nieznana')
            else:
                g_date_add.config(text='Zmien date')
                d = date_list[1]
                if len(d) == 1:
                    d = '0' + date_list[1]
                m = date_list[0]
                if len(m) == 1:
                    m = '0' + date_list[0]
                y = date_list[2]
                g_date.config(text=f'Data zdobycia: {d}.{m}.20{y}')


def show_cal():
    global root2
    global cal
    today = str(date.today())
    today_y = int(today[0:4])
    today_m = int(today[5:7])
    today_d = int(today[8:])
    root2 = Tk()
    root2.title('Kalendarz')
    cal = Calendar(root2, expand=True, selectmode='day',
                   year=today_y, month=today_m, day=today_d, mindate=date(2000, 1, 1), maxdate=datetime.now())
    cal.pack()
    butt_deldate = Button(root2, text="Usun date zdobycia", command=del_date)
    butt_deldate.pack(side=BOTTOM, fill='x')

    butt_grabdate = Button(root2, text="Zapisz date zdobycia", command=grab_date)
    butt_grabdate.pack(side=BOTTOM, fill='x')

    if 'nieznana' in g_date.cget('text'):
        butt_deldate.config(state=DISABLED)
    else:
        butt_deldate.config(state=NORMAL)
    root2.attributes('-topmost', True)
    #root2.mainloop


def grab_date():
    with open('savestate_date.txt') as file2:
        line_edit = file2.readlines()
        line_edit[i_displayed] = cal.get_date() + '\n'
    with open('savestate_date.txt', 'w') as file2:
        file2.writelines(line_edit)
    check_date()
    g_date_add.config(text='Zmien date')
    root2.destroy()
    g_date.grid(row=4, column=0, sticky=W, padx=20, pady=10)
    check_last_peak()


def del_date():
    warn_del_date = messagebox.askyesno(title='Uwaga!',
                                        message='Czy na pewno chcesz usunac zapisana date zdobycia szczytu?',
                                        icon='warning')
    if warn_del_date:
        with open('savestate_date.txt') as file2:
            line_edit = file2.readlines()
            line_edit[i_displayed] = 'nieznana' + '\n'
        with open('savestate_date.txt', 'w') as file2:
            file2.writelines(line_edit)
        check_date()
        check_last_peak()
        g_date_add.config(text='Dodaj date')
        root2.destroy()


path_main = 'INSERT MAIN KORONAAPP DIRECTORY PATH'

root = Tk()
root.title('KORONA APP')
root.geometry('500x500')
root.iconphoto(True, PhotoImage(file=f'{path_main}\\images\\rooticon.png'))

notebook = ttk.Notebook(root)
tab1 = Frame(notebook, bg='white')
tab2 = Frame(notebook, bg='white')
tab3 = Frame(notebook, bg='white')
tab4 = Frame(notebook, bg='white')

notebook.add(tab1, text='Strona glowna')
notebook.add(tab3, text='Szczyty')
notebook.add(tab2, text='Testy')
# notebook.add(tab4, text='Mapa')
notebook.pack(expand=True, fill='both')
# _______________________________________________________________________________
# TAB1
all_peak = Label(tab1, text='Zdobyte szczyty :', bg='white')
all_peak.grid(sticky='W', padx=10, pady=5, row=0, column=0)
all_peak_inf = Label(tab1, text='0/28', bg='white')
all_peak_inf.grid(sticky='W', pady=5, row=0, column=1)

high_peak = Label(tab1, text='Najwyzszy zdobyty szczyt :', bg='white')
high_peak.grid(sticky='W', padx=10, pady=5, row=1, column=0)
high_peak_inf = Label(tab1, text='', bg='white')
high_peak_inf.grid(sticky='W', pady=5, row=1, column=1)

last_peak = Label(tab1, text='Ostatni zdobyty szczyt :', bg='white')
last_peak.grid(sticky='W', padx=10, pady=5, row=2, column=0)
last_peak_inf = Label(tab1, text='', bg='white')
last_peak_inf.grid(sticky='W', pady=5, row=2, column=1)
# _______________________________________________________________________________
# TAB 2
x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14,\
    x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),\
    IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),\
    IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),\
    IntVar()

list_x = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16,
          x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27]

g0 = g1 = g2 = g3 = g4 = g5 = g6 = g7 = g8 = g9 = g10 = g11 = g12 = g13 = g14 = g15 =\
    g16 = g17 = g18 = g19 = g20 = g21 = g22 = g23 = g24 = g25 = g26 = g27 = None

text_list = [g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16,
             g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27]

count = -1
count_row = -0.25
count_name = -1
with open(f'{path_main}\\data.txt') as file:
    name_list = []
    for i, line in enumerate(file):
        name_list.append(line)

for i in text_list:
    count += 1
    count_name += 1
    if count == 4:
        count = 0
    count_row += 0.25
    if count_name >= 15:
        count_split = -5
    else:
        count_split = -6
    butt = Checkbutton(tab2, text=name_list[count_name][0:count_split],
                       variable=list_x[count_name],
                       command=check_peak,
                       bg='white')
    butt.grid(row=count_row.__floor__(), column=count, sticky='W')

boot()
# _______________________________________________________________________________
# TAB Szczyty

gora = StringVar()
gora.set('Wybierz szczyt')

with open(f'{path_main}\\data.txt') as file:
    name_list_edit = []
    for i, line in enumerate(file):
        if i <= 13:
            name_list_edit.append(line[0:-6])
        else:
            name_list_edit.append(line[0:-5])

drop = OptionMenu(tab3, gora, *name_list_edit, command=display)
drop.config(width=17)
drop.grid(row=0, column=0, padx=20, pady=20)

separator = ttk.Separator(tab3, orient='horizontal')
separator.place(x=0, y=70, relwidth=1)

g_name = Label(tab3, text='', bg='white')
g_name.grid(row=2, column=0, sticky=W, padx=20, pady=10)

g_height = Label(tab3, text='', bg='white')
g_height.grid(row=3, column=0, sticky=W, padx=20, pady=10)

g_date = Label(tab3, text=f'Data zdobycia: ', bg='white')
g_date_add = Button(tab3, text='Dodaj date', bg='white', command=show_cal, width=10)

# API
g_travel = Label(tab3, text='Dane dojazdowe:', bg='white')  # , font='15')
g_distance = Label(tab3, text='Dystans:', bg='white')
# g_distance.grid(row=5, column=0, sticky=W, padx=20, pady=10)
g_time = Label(tab3, text='Czas dojazdu', bg='white')
# g_time.grid(row=5, column=1, sticky=W, padx=20, pady=10)


root.mainloop()
