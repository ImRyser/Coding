from tkinter import *

# quit button
def quit_app():
    main_window.destroy()

# add and display data
def entry_print():
    global hire_details, total_entries

    # add new entry
    hire_details.append([
        entry_full_name.get(),
        entry_receipt_number.get(),
        entry_item_hired.get(),
        entry_number_hired.get()
    ])
    total_entries += 1

    # clear previous display
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) >= 8:
            widget.destroy()

    # display all entries
    for i in range(total_entries):
        Label(main_window, text=str(i)).grid(column=0, row=i+8)
        Label(main_window, text=hire_details[i][0]).grid(column=1, row=i+8)
        Label(main_window, text=hire_details[i][1]).grid(column=2, row=i+8)
        Label(main_window, text=hire_details[i][2]).grid(column=3, row=i+8)
        Label(main_window, text=hire_details[i][3]).grid(column=4, row=i+8)

# clear input fields
def append_name():
    entry_full_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    entry_number_hired.delete(0, 'end')

# delete row
def delete_row():
    global hire_details, total_entries

    try:
        index = int(entry_row.get())
        if 0 <= index < total_entries:
            hire_details.pop(index)
            total_entries -= 1
            entry_row.delete(0, 'end')
            refresh_display()
    except ValueError:
        print("Invalid row number")

# refresh table display
def refresh_display():
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) >= 8:
            widget.destroy()

    for i in range(total_entries):
        Label(main_window, text=str(i)).grid(column=0, row=i+8)
        Label(main_window, text=hire_details[i][0]).grid(column=1, row=i+8)
        Label(main_window, text=hire_details[i][1]).grid(column=2, row=i+8)
        Label(main_window, text=hire_details[i][2]).grid(column=3, row=i+8)
        Label(main_window, text=hire_details[i][3]).grid(column=4, row=i+8)

# UI setup
def setup_buttons():
    global entry_full_name, entry_receipt_number, entry_item_hired, entry_number_hired, entry_row

    Label(main_window, text="Customer Name").grid(column=0, row=2)
    entry_full_name = Entry(main_window)
    entry_full_name.grid(column=2, row=2)

    Label(main_window, text="Receipt Number").grid(column=0, row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=2, row=3)

    Label(main_window, text="Item Hired").grid(column=0, row=4)
    entry_item_hired = Entry(main_window)
    entry_item_hired.grid(column=2, row=4)

    Label(main_window, text="Number Hired").grid(column=0, row=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=2, row=5)

    Label(main_window, text="Row ").grid(column=4, row=2)
    entry_row = Entry(main_window)
    entry_row.grid(column=5, row=2)

    Button(main_window, text="Print", command=entry_print).grid(column=3, row=1)
    Button(main_window, text="Append Details", command=append_name).grid(column=4, row=1)
    Button(main_window, text="Delete Row", command=delete_row).grid(column=6, row=2)
    Button(main_window, text="Quit", command=quit_app).grid(column=5, row=1)

    # headers
    Label(main_window, text="Row", font='bold').grid(column=0, row=7)
    Label(main_window, text="Customer Name", font='bold').grid(column=1, row=7)
    Label(main_window, text="Receipt Number", font='bold').grid(column=2, row=7)
    Label(main_window, text="Item Hired", font='bold').grid(column=3, row=7)
    Label(main_window, text="Number Hired", font='bold').grid(column=4, row=7)

# main
def main():
    global main_window, hire_details, total_entries
    hire_details = []
    total_entries = 0

    main_window = Tk()
    setup_buttons()
    main_window.mainloop()

main()