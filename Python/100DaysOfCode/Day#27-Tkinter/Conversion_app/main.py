from tkinter import *

window = Tk()
window.minsize(width=200, height=100)
window.title('Miles 2 Kilometers')
window.config(padx=10, pady=10)


# Input
input = Entry(width=10)
input.grid(column=1, row=0)


# Labels
miles = Label(text='Miles')
miles.grid(column=2, row=0)
equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)
answer = Label(text='0')
answer.grid(column=1, row=1)
kilo = Label(text='Km')
kilo.grid(column=2, row=1)



def xfer():
    m = int(input.get())
    print(m)
    k = round(m * 1.609)
    answer.config(text=str(k))


# Button
button = Button(text='Calculate', command=xfer)
button.grid(column=1, row=2)


window.mainloop()
