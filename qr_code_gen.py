import pyqrcode
from tkinter import *
from PIL import ImageTk, Image
import time

def qr_code(data):
    root = Tk()
    canvas = Canvas(root, width=400, height=400)
    canvas.pack()
    code = pyqrcode.create(data)
    code.png(f'qrcode_{time.strftime("%Y%m%d")}.png', scale=8)
    img_to_display = ImageTk.PhotoImage(Image.open(f'qrcode_{time.strftime("%Y%m%d")}.png'))
    canvas.create_image(40, 40, anchor=NW, image=img_to_display)
    root.mainloop()

if __name__ == "__main__":
    data = input("Enter the link:") # Or simply put the data here
    qr_code(data)