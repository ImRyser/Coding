from tkinter import *

def quit():
    main_window.destroy()


def print_names ():
    name_count = 0
    Label(main_window, font='bold',text="Row").grid(column=0,row=6)
    Label(main_window, font='bold',text="Name").grid(column=1,row=6)
    Label(main_window, font='bold',text="Age").grid(column=2,row=6)
    Label(main_window, font='bold',text="Gender").grid(column=3,row=6)
    ROWS_ABOVE = 7
    while name_count < counters['total entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+7)
        Label(main_window, text=(j_names[name_count][0])).grid(column=1,row=name_count+ROWS_ABOVE)
        Label(main_window, text=(j_names[name_count][1])).grid(column=2,row=name_count+ROWS_ABOVE)
        Label(main_window, text=(j_names[name_count][2])).grid(column=3,row=name_count+ROWS_ABOVE)
        name_count +=1

def append_name ():
    j_names.append([entry_name.get(),entry_age.get(),entry_gender.get()])