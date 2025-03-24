from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Traffic data on Histogram")
root.iconbitmap("C:/Users/hp/Downloads/traffic data/statistic_9684905.ico")

frame = LabelFrame(root, text= "Histogram....", padx=40, pady=40, relief =SUNKEN )
frame.pack(padx=10, pady = 10)


my_img_1 = ImageTk.PhotoImage(Image.open("images/histogram.PNG"))

my_label = Label(frame, image= my_img_1)
my_label.grid(row=3, column=0, columnspan =3)
















root.mainloop()
