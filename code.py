#used to open application
from tkinter import*
import random

#used to create a "quit" button
def quit():
    main_window.destroy

#used to create a "print" button
def entry_print():
    global hire_details, total_entries
    name_count = 0
    Label(main_window,text= entry_full_name.get()).grid(column=1,row=7,sticky=E)
    Label(main_window,text=entry_receipt_number.get()).grid(column=2,row=7)
    Label(main_window,text=entry_item_hired.get()).grid(column=3,row=7)
    Label(main_window,text=entry_number_hired.get()).grid(column=4,row=7)
    #used to give "Row #" number
    Label(main_window,text="1").grid()
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0,row=name_count+7)
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1,row=name_count+name_count+6)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2,row=name_count+name_count+6)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2,row=name_count+name_count+6)
        name_count +=1

#used to create a "append" button
def append_name ():
    global hire_details, entry_full_name,entry_receipt_number,entry_item_hired,entry_number_hired, total_entries
    hire_details.append([entry_full_name.get(),entry_receipt_number.get(),entry_item_hired.get(),entry_number_hired.get()])
    entry_full_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_item_hired.delete(0,'end')
    entry_number_hired.delete(0,'end')
    total_entries +=1


#used to give random receipt number
def generate_random():
    random_number = random.randint(1,10)
    Label(main_window,text=random_number).grid(column=0,row=2, sticky=E)

#adds buttons and titles to the main window
def setup_buttons():
    global hire_details, entry_full_name,entry_receipt_number,entry_item_hired,entry_number_hired, total_entries
    Button(main_window, text="Append Details",command=append_name).grid(column=3,row=1)
    Button(main_window, text="Quit",command= quit) .grid(column=5,row=1)
    Button(main_window, text="Print Details",command=entry_print).grid(column=4,row=1)
    Button(main_window, text="Delete Row",).grid(column=6,row=2)
    Label(main_window,text="Customer Name").grid(column=0,row=2)
    entry_full_name = Entry(main_window)
    entry_full_name.grid(column=2,row=2,padx=10,pady=5)
    Label(main_window,text="Receipt Number").grid(column=0,row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=2,row=3,padx=10,pady=5)
    Label(main_window,text="Item Hired").grid(column=0,row=4)
    entry_item_hired = Entry(main_window)
    entry_item_hired.grid(column=2,row=4,padx=10,pady=5)
    Label(main_window,text="Number Hired").grid(column=0,row=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=2,row=5,padx=10,pady=5)    
    entry_row = Entry(main_window)
    entry_row.grid(column=5,row=2,padx=15,pady=5)
    Label(main_window,font='bold',text="Row").grid(column=0,row=6)
    Label(main_window,font='bold',text="Customer Name").grid(column=1,row=6)
    Label(main_window,font='bold',text="Receipt Number").grid(column=2,row=6)
    Label(main_window,font='bold',text="Hire Item").grid(column=3,row=6,padx=10)
    Label(main_window,font='bold',text="Number Hired").grid(column=4,row=6,padx=15)
    Label(main_window,text="Row #").grid(column=4,row=2,padx=5)
   

def main():
    global main_window
    global hire_details, entry_full_name, entry_receipt_number, entry_item_hired, entry_number_hired, total_entries
    hire_details = []
    total_entries = 0
    main_window =Tk()   
    setup_buttons()
    main_window.mainloop()

main()