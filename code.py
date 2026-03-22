# used to open application
from tkinter import *

# used to create a "quit" button
def quit():
    main_window.destroy()

# used to create a "print" button
def entry_print():
    global hire_details, total_entries
    # clear previous labels for the display
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) >= 8:
            widget.destroy()
    
    # display all hire details
    for i in range(total_entries):
        Label(main_window, text=str(i)).grid(column=0, row=i+8)
        Label(main_window, text=hire_details[i][0]).grid(column=1, row=i+8)
        Label(main_window, text=hire_details[i][1]).grid(column=2, row=i+8)
        Label(main_window, text=hire_details[i][2]).grid(column=3, row=i+8)
        Label(main_window, text=hire_details[i][3]).grid(column=4, row=i+8)

# used to create an "append" button
def append_name():
    global hire_details, entry_full_name, entry_receipt_number, entry_item_hired, entry_number_hired, total_entries
    hire_details.append([
        entry_full_name.get(),
        entry_receipt_number.get(),
        entry_item_hired.get(),
        entry_number_hired.get()
    ])
    entry_full_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_item_hired.delete(0,'end')
    entry_number_hired.delete(0,'end')
    total_entries += 1
    entry_print()  # automatically refresh display

# used to delete a specific row
def delete_row():
    global hire_details, total_entries, entry_row
    try:
        index = int(entry_row.get())
        hire_details.pop(index)
        total_entries -= 1
        entry_row.delete(0,'end')
        entry_print()
    except:
        pass

# adds buttons and titles to the main window
def setup_buttons():
    global hire_details, entry_full_name, entry_receipt_number, entry_item_hired, entry_number_hired, entry_row
    # input labels and entries
    Label(main_window, text="Customer Name").grid(column=0, row=2)
    entry_full_name = Entry(main_window)
    entry_full_name.grid(column=2, row=2, padx=10, pady=5)
    Label(main_window, text="Receipt Number").grid(column=0, row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=2, row=3, padx=10, pady=5)
    Label(main_window, text="Item Hired").grid(column=0, row=4)
    entry_item_hired = Entry(main_window)
    entry_item_hired.grid(column=2, row=4, padx=10, pady=5)
    Label(main_window, text="Number Hired").grid(column=0, row=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=2, row=5, padx=10, pady=5)
    # Row number input for deletion
    Label(main_window, text="Row # to Delete").grid(column=4, row=2)
    entry_row = Entry(main_window)
    entry_row.grid(column=5, row=2, padx=5, pady=5)
    # buttons
    Button(main_window, text="Append Details", command=append_name).grid(column=3, row=1)
    Button(main_window, text="Delete Row", command=delete_row).grid(column=6, row=2)
    Button(main_window, text="Quit", command=quit).grid(column=5, row=1)
    Button(main_window, text="Print Details", command=entry_print).grid(column=4, row=1)
    # table headers
    Label(main_window, font='bold', text="Row").grid(column=0, row=7)
    Label(main_window, font='bold', text="Customer Name").grid(column=1, row=7)
    Label(main_window, font='bold', text="Receipt Number").grid(column=2, row=7)
    Label(main_window, font='bold', text="Item Hired").grid(column=3, row=7, padx=10)
    Label(main_window, font='bold', text="Number Hired").grid(column=4, row=7, padx=15)
# main function
def main():
    global main_window, hire_details, total_entries
    hire_details = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()

main()