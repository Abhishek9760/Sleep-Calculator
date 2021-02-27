import tkinter, sys, os
from tkinter import END
from datetime import datetime
from functools import partial


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


icon_path = resource_path("icon.ico")

root = tkinter.Tk()
root.title("sleep calculator")
root.iconbitmap(icon_path)
root.config(bg="#999")
root.geometry("500x400")
root.resizable(0, 0)

# functions
def calc_sleep_hours():
    try:
        birth_date = datetime(int(year.get()), int(month.get()), int(day.get()))
        current_date = datetime(int(year2.get()), int(month2.get()), int(day2.get()))
    except Exception as e:
        toplevel = tkinter.Toplevel(root)
        toplevel.iconbitmap(icon_path)
        toplevel.resizable(0, 0)
        tkinter.Label(toplevel, text=e, font=("Arial", 15, "bold")).pack(
            padx=20, pady=20
        )
    delta = current_date - birth_date
    total_days = delta.days
    alive_days = (delta.total_seconds() // 3600 - 8 * total_days) // 24
    sleep_hours = 8 * total_days

    # labels
    alive_label = result_label(text=f"You have been alive for {int(alive_days)} days")
    sleep_label = result_label(text=f"You have slept {sleep_hours} hours")
    alive_label.grid(row=0, column=1, sticky="E", ipadx=5, ipady=5)
    sleep_label.grid(row=1, column=1, sticky="E", ipadx=5, ipady=5)

    # clearing the inputs
    day.delete(0, END)
    month.delete(0, END)
    year.delete(0, END)


# Label
def create_label(text, frame, font, fg):
    return tkinter.Label(frame, text=text, font=font, fg=fg)


# Entry
def create_entry(frame, width, borderwidth):
    return tkinter.Entry(frame, width=width, borderwidth=borderwidth)


# button
def create_button(frame, text, command, bg, fg, borderwidth):
    return tkinter.Button(
        frame, text=text, command=command, bg=bg, fg=fg, borderwidth=borderwidth
    )


# Frames
title_frame = tkinter.Frame(root, height=80, width=500)
title_frame.pack(pady=(0, 2), fill="both")
controller_frame = tkinter.Frame(root, height=350, width=500)
controller_frame.pack(fill="both")
result_frame = tkinter.Frame(root, height=70, width=500)
result_frame.pack(pady=(2, 0), fill="both", expand=True)

# Partials
controller_label = partial(
    create_label, font=("Arial", 10, "bold"), frame=controller_frame, fg=None
)
controller_entry = partial(create_entry, frame=controller_frame, width=5, borderwidth=3)
result_button = partial(create_button, borderwidth=3, frame=result_frame, fg="#fff")
result_label = partial(
    create_label, frame=result_frame, font=("Cambria", 10, "italic"), fg=None
)

# title
sleep_title = create_label(
    frame=title_frame, text="Sleep Calculator", fg="blue", font=("Arial", 20, "bold")
)
sleep_title.pack(pady=20)
title_frame.pack_propagate(0)


# entry labels
birthdate_label = controller_label(text="Enter your Birthdate", fg="black")
birthdate_label.grid(row=0, column=0, columnspan=2, sticky="W", pady=(20, 0), padx=60)

date_label = controller_label(text="Enter today's date", fg="black")
date_label.grid(row=0, column=3, columnspan=2, sticky="E", pady=(20, 0), padx=(0, 70))


# inputs and their labels
day_label = controller_label(text="Day")
day_label.grid(row=1, column=0, pady=20)
day = controller_entry()
day.grid(row=1, column=1, pady=20, ipady=2)

month_label = controller_label(text="Month")
month_label.grid(row=2, column=0, pady=(0, 20))
month = controller_entry()
month.grid(row=2, column=1, pady=(0, 20), ipady=2)

year_label = controller_label(text="Year")
year_label.grid(row=3, column=0, pady=(0, 20))
year = controller_entry()
year.grid(row=3, column=1, pady=(0, 20), ipady=2)

day_label = controller_label(text="Day")
day_label.grid(row=1, column=3, pady=20)
day2 = controller_entry()
day2.grid(row=1, column=4, pady=20, ipady=2)
day2.insert(END, datetime.now().day)

month_label = controller_label(text="Month")
month_label.grid(row=2, column=3, pady=(0, 20))
month2 = controller_entry()
month2.grid(row=2, column=4, pady=(0, 20), ipady=2)
month2.insert(END, datetime.now().month)

year_label = controller_label(text="Year")
year_label.grid(row=3, column=3, pady=(0, 20))
year2 = controller_entry()
year2.grid(row=3, column=4, pady=(0, 20), ipady=2)
year2.insert(END, datetime.now().year)


# result buttons
calc_button = result_button(text="Calculate", command=calc_sleep_hours, bg="#313")
calc_button.grid(row=0, column=0, ipadx=2, ipady=2, pady=10, padx=(20, 160))

exit_button = result_button(text="Exit", command=lambda: root.destroy(), bg="#222")
exit_button.grid(row=1, column=0, sticky="W", ipadx=2, padx=(20, 160))


root.mainloop()