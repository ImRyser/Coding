from tkinter import *
from tkinter import messagebox  

# quit button
def quit_app():
    main_window.destroy()

# print stored data
def entry_print():
    refresh_display()

# append (store data)
def append_name():
    global hire_details, total_entries

    # -------- VALIDATION -------- #

    # Customer Name (no numbers allowed)
    name = entry_full_name.get().strip()
    if name == "":
        messagebox.showerror("Error", "Customer Name is required")
        return
    if any(char.isdigit() for char in name):
        messagebox.showerror("Error", "Customer Name cannot contain numbers")
        return

    # Receipt Number (must be number)
    if not entry_receipt_number.get().isdigit():
        messagebox.showerror("Error", "Receipt Number must be a number")
        return

    # Item Hired (no numbers allowed)
    item = entry_item_hired.get().strip()
    if item == "":
        messagebox.showerror("Error", "Item Hired is required")
        return
    if any(char.isdigit() for char in item):
        messagebox.showerror("Error", "Item Hired cannot contain numbers")
        return

    # Number Hired
    try:
        num_hired = int(entry_number_hired.get())
        if not (1 <= num_hired <= 500):
            messagebox.showerror("Error", "Number Hired must be between 1 and 500")
            return
    except ValueError:
        messagebox.showerror("Error", "Number Hired must be a number")
        return

    # Date Hired
    if entry_date_hired.get().strip() == "":
        messagebox.showerror("Error", "Date Hired is required")
        return

    # Return Date
    if entry_date_return.get().strip() == "":
        messagebox.showerror("Error", "Return Date is required")
        return

    # -------- STORE DATA -------- #
    hire_details.append([
        name,
        entry_receipt_number.get(),
        item,
        str(num_hired),
        entry_date_hired.get(),
        entry_date_return.get(),
    ])
    total_entries += 1

    # clear input fields
    entry_full_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    entry_number_hired.delete(0, 'end')
    entry_date_hired.delete(0, 'end')
    entry_date_return.delete(0, 'end')

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
        else:
            messagebox.showerror("Error", "Row does not exist")
    except ValueError:
        messagebox.showerror("Error", "Row must be a number")

# refresh table display
def refresh_display():
    # clear old table
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) >= 9:
            widget.destroy()

    # display updated table
    for i in range(total_entries):
        Label(main_window, text=str(i)).grid(column=0, row=i+9)
        Label(main_window, text=hire_details[i][0]).grid(column=1, row=i+9)
        Label(main_window, text=hire_details[i][1]).grid(column=2, row=i+9)
        Label(main_window, text=hire_details[i][2]).grid(column=3, row=i+9)
        Label(main_window, text=hire_details[i][3]).grid(column=4, row=i+9)
        Label(main_window, text=hire_details[i][4]).grid(column=5, row=i+9)
        Label(main_window, text=hire_details[i][5]).grid(column=6, row=i+9)

# UI setup
def setup_buttons():
    global entry_full_name, entry_receipt_number, entry_item_hired
    global entry_number_hired, entry_row, entry_date_hired, entry_date_return

    # Input fields
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

    Label(main_window, text="Date Hired").grid(column=0, row=6)
    entry_date_hired = Entry(main_window)
    entry_date_hired.grid(column=2, row=6)

    Label(main_window, text="Return Date").grid(column=0, row=7)
    entry_date_return = Entry(main_window)
    entry_date_return.grid(column=2, row=7)

    # row delete input
    Label(main_window, text="Row").grid(column=4, row=2)
    entry_row = Entry(main_window)
    entry_row.grid(column=5, row=2)

    # buttons
    Button(main_window, text="Append Details", command=append_name).grid(column=3, row=1)
    Button(main_window, text="Print", command=entry_print).grid(column=4, row=1)
    Button(main_window, text="Delete Row", command=delete_row).grid(column=6, row=2)
    Button(main_window, text="Quit", command=quit_app).grid(column=5, row=1)

    # table headers
    Label(main_window, text="Row").grid(column=0, row=8)
    Label(main_window, text="Customer Name").grid(column=1, row=8)
    Label(main_window, text="Receipt Number").grid(column=2, row=8)
    Label(main_window, text="Item Hired").grid(column=3, row=8)
    Label(main_window, text="Number Hired").grid(column=4, row=8)
    Label(main_window, text="Date Hired").grid(column=5, row=8)
    Label(main_window, text="Return Date").grid(column=6, row=8)

# main
def main():
    global main_window, hire_details, total_entries
    hire_details = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()

main()