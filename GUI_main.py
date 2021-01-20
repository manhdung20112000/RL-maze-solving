import tkinter as tk

window = tk.Tk()
window.title("Application")
window.geometry('800x600')

label = tk.Label(window, text="Hello, Tkinter")
label.grid(column=0, row=0)

def submit():
    label.configure(text="Clicked!")

btn = tk.Button(window, text="Submit input", command=submit)
btn.grid(column=0, row=1)

window.mainloop()