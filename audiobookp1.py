import tkinter as tk
import time
from tkinter.ttk import Progressbar
from tkinter import *

# Initialize main app window
app = tk.Tk()
app.geometry('995x650')
app.config(bg='#000428')
app.title("Audio Book")
app.resizable(False, False)

# Function to open next window
def new():
    app.destroy()
    import audiobookp5  # Ensure this file exists before importing

# ------------------------------------------ Loading Progress Bar
def step_progress(per=0):
    """Updates progress bar in steps."""
    if per <= 100:
        pb1['value'] = per
        label11.config(text=f"{per} %")
        app.after(1000, step_progress, per + 20)
    else:
        new()

pb1 = Progressbar(app, orient=HORIZONTAL, length=800, mode='determinate')
pb1.place(x=100, y=520)

label10 = tk.Label(app, text='Loading...', fg='white', bg='#000428')
label10.place(x=100, y=550)

label11 = tk.Label(app, text='', fg='white', font='Arial 10 bold', bg='#000428')
label11.place(x=900, y=520)

# ------------------------------------------ Welcome Animation
def animate_text(label, text, index=0):
    """Animates text letter by letter."""
    if index < len(text):
        label.config(text=text[:index + 1])
        app.after(250, animate_text, label, text, index + 1)

# Welcome Labels
label1 = tk.Label(app, text='', font='Algerian 50 bold', fg='white', bg='#000428')
label1.place(x=100, y=350)
app.after(500, animate_text, label1, "Welcome")

label3 = tk.Label(app, text='', font='Algerian 40 bold', fg='white', bg='#000428')
label3.place(x=420, y=350)
app.after(1500, animate_text, label3, "To")

label5 = tk.Label(app, text='', font='Algerian 40 bold', fg='white', bg='#000428')
label5.place(x=540, y=350)
app.after(2500, animate_text, label5, "Audio")

label7 = tk.Label(app, text='', font='Algerian 40 bold', fg='white', bg='#000428')
label7.place(x=740, y=350)
app.after(3500, animate_text, label7, "Book")

# ------------------------------------------ Logo & Version
try:
    logo_img = tk.PhotoImage(file='./images/output-onlinepngtools (21).png')
    Label9 = tk.Label(app, image=logo_img, border=0)
    Label9.image = logo_img  # Prevent garbage collection
    Label9.place(x=350, y=30)
except Exception as e:
    print(f"Error loading image: {e}")

label10 = tk.Label(app, text='Version 1.0', fg='white', bg='#000428')
label10.place(x=470, y=300)

# Start progress bar
app.after(4000, step_progress)  # Starts progress after animation

app.mainloop()
