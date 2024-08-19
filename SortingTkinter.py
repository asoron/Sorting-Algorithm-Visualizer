import tkinter as tk
from tkinter import ttk
import time
import Sorting
from config import *

root = tk.Tk()
root.geometry(str(state.screenWidth)+"x"+str(state.screenHeight+50))
root.configure(bg=state.background)
root.title("Sorting Algorithm Visualizer")

combobox = ttk.Combobox(root, values=Sorting.shortingAlgorithms)
combobox.set("Choose Sorting Algorithm")
combobox.pack(pady=10)

canvas = tk.Canvas(root, width=state.screenWidth, height=state.screenHeight, bg=state.background)
canvas.pack()


def on_select(event):
    print("Before array creation:", state.unsorted_array)
    state.create_new_array(canvas)  
    createVisual(canvas, state.unsorted_array)
    print("After array creation:", state.unsorted_array)
    func = getattr(Sorting, combobox.get())
    func(state.unsorted_array,updateColor,updateVisual)
    print("After sorting:", state.unsorted_array)

combobox.bind("<<ComboboxSelected>>", on_select)

def createVisual(canvas,data):
    for i in range(len(data)):
        state.canvases.append(canvas.create_rectangle(i*(state.screenWidth/state.arrayLength), state.screenHeight, ((state.screenWidth/state.arrayLength)*(4/5))+i*(state.screenWidth/state.arrayLength), state.screenHeight-state.scaledData[i], fill=state.baseColor))

def updateVisual(choosenIndex, swapIndex):
    canvas.itemconfig(state.canvases[choosenIndex], fill=state.swapColor)
    canvas.itemconfig(state.canvases[swapIndex], fill=state.swapColor)
    
    root.update()
    time.sleep(0.05)
    
    state.scaledData[choosenIndex], state.scaledData[swapIndex] = state.scaledData[swapIndex],state.scaledData[choosenIndex]
    canvas.coords(state.canvases[choosenIndex],choosenIndex*(state.screenWidth/state.arrayLength), state.screenHeight, ((state.screenWidth/state.arrayLength)*(4/5))+choosenIndex*(state.screenWidth/state.arrayLength), state.screenHeight-state.scaledData[choosenIndex])
    canvas.coords(state.canvases[swapIndex],swapIndex*(state.screenWidth/state.arrayLength), state.screenHeight, ((state.screenWidth/state.arrayLength)*(4/5)) +swapIndex*(state.screenWidth/state.arrayLength), state.screenHeight-state.scaledData[swapIndex])

    root.update()
    time.sleep(0.05)
    
    canvas.itemconfig(state.canvases[choosenIndex], fill=state.baseColor)
    canvas.itemconfig(state.canvases[swapIndex], fill=state.baseColor)
    root.update()


def updateColor(index,green):
    if(green):
        canvas.itemconfig(state.canvases[index], fill=state.sortedColor)
    else:
        canvas.itemconfig(state.canvases[index], fill=state.baseColor)
        
    root.update()

root.mainloop()