from tkinter import *
from PIL import Image, ImageTk
import time

root = Tk()

root.title("Slideshow Widget")

image1 = ImageTk.PhotoImage(Image.open("image1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("image2.jpeg"))
image3 = ImageTk.PhotoImage(Image.open("image3.jpg"))

image_arr = [image1, image2, image3]


pic_label = Label(root)

pic_label.pack()


while True:

    for i in range(len(image_arr)):

        pic_label.config(image=image_arr[i])

        root.update()

        time.sleep(2)

root.mainloop()
