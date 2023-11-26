from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
current_text = ''
count_down_timer = None
count = 5

# ---------------------------- FUNCTIONS ------------------------------- #
def on_entry_change():
    global current_text, count_down_timer, count
    # print(entry.get())
    # print(current_text)
    canvas.itemconfig(timer_txt, text=f"{count}")
    
    if len(entry.get()) > 0 and current_text == entry.get():
        if count > 0:
            window.after(1000, on_entry_change)
            count -= 1
        else:
            entry.delete(0, END)
            canvas.itemconfig(timer_txt, text='5')
            count = 5  # Reset count to 5
            window.after(1000, on_entry_change)
    else:
        current_text = entry.get()
        count = 5
        window.after(1000, on_entry_change)

# ---------------------------- GUI SETUP ------------------------------- #
window = Tk()
window.title("Dangerous Typing App")
window.config(padx=50, pady=50)


# Entry
entry = Entry(fg='black', font=('Arial', 20), width=24,  insertwidth=4)
entry.grid(row=1, column=0, columnspan=3, pady=10)

# Label
title_txt = Label(text='Dangerous Typing App', font=('Futura', 32), fg= 'white',bg='red')
title_txt.grid(row=0, column=0, columnspan=3, pady=10)

# Canvas
canvas = Canvas(width=50, height=25)
timer_txt = canvas.create_text(25, 10, text="5", fill='black', font=(FONT_NAME, 16, "bold"))
canvas.grid(row=2, column=1, pady=10)

on_entry_change()
window.mainloop()
