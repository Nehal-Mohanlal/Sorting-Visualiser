from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort

root = Tk()
root.title('visualiser')
root.maxsize(1100, 900)
root.config(bg='black')

selected_alg = StringVar()
data =[]

def drawData(data,colorArray):
    c.delete('all')
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 5
    normdata = [i / max(data) for i in data]
    for i, height in enumerate(normdata):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        c.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        c.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

def Generate():
    global data
    min = int(minEntry.get())

    max = int(maxEntry.get())

    size = int(sizeEntry.get())

    data = []
    for i in range(size):
        data.append(random.randrange(min, max + 1))
    drawData(data, ["red" for x in range (len(data))])


def startalgorithm():
    global data
    bubble_sort(data, drawData)


# frame base layout
UI_Frame = Frame(root, width=600, height=200, bg='grey')
UI_Frame.grid(row=0, column=0, padx=10, pady=5)

c = Canvas(root, width=600, height=380, bg='white')
c.grid(row=1, column=0, padx=10, pady=5)

# user interface
# row[0]
Label(UI_Frame, text='Algorithm ', bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algmenu = ttk.Combobox(UI_Frame, textvariable=selected_alg, values=['bubble sort', 'merge sort'])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)
speedscale = Scale(UI_Frame, from_=0.1, to=6.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label=("select speed [s] "))
speedscale.grid(row=0, column=2, padx=5, pady=5)

Button(UI_Frame, text="start", command=startalgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

# row[1]

sizeEntry = speedscale = Scale(UI_Frame, from_=3, to=50, resolution=1, orient=HORIZONTAL, label=("select size"))
sizeEntry.grid(row=1, column=0, padx=5, pady=5, )

minEntry = speedscale = Scale(UI_Frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label=("select min value "))
minEntry.grid(row=2, column=1, padx=5, pady=5, )

maxEntry = speedscale = Scale(UI_Frame, from_=10, to=100, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                              label=("select max value "))
maxEntry.grid(row=1, column=2, padx=5, pady=5, )

Button(UI_Frame, text="generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)
root.mainloop()
