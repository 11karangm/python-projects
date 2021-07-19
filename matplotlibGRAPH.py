from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("3")
root.geometry("700x200")

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.hist(house_prices,50)
    plt.show()

callw = Button(root,text="call me",command = graph).pack()

root.mainloop()