from tkinter import *

def convert():
    conversion=float(input.get()) / 1.609
    text.config(text=f"Km is equal to {conversion:.2f} Miles")


window=Tk()
window.title("KM to Miles Converter")
window.minsize(200,100)
window.config(padx=20,pady=20)

input=Entry(width=5)
input.grid(column=4,row=1)
input.insert(END, string=0)

text=Label(text="Km is equal to 0 Miles")
text.grid(column=5,row=1)

button=Button(text="Convert",command=convert)
button.grid(column=5,row=2)

window.mainloop()