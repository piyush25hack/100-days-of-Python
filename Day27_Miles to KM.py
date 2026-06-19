from tkinter import *

def miletokm():
    miles = float(mile.get())
    km = round(miles * 1.609)
    # 'result' label ko update karein, 'label_km' ko nahi
    result.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

mile = Entry(width=10, bg = "Red")
mile.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

iqt = Label(text="is equal to")
iqt.grid(column=0, row=1)

# Ye label badlega
result = Label(text="0")
result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

Btn = Button(text="Calculate", command=miletokm)
Btn.grid(column=1, row=2)

window.mainloop()