import tkinter as tk
from prng import random_generator
from PIL import ImageTk, Image
# from pathlib import Path
from imageservice import get_image_path

def next_image(panel):
    random_number = random_generator()
    path = get_image_path(random_number)

    my_image = Image.open(path)
    my_image = my_image.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(my_image)
    panel.configure(image=img)
    panel.image = img

def user_interface():
    window = tk.Tk()

    greeting = tk.Label(text="Welcome to the random cat image generator!")
    greeting.pack()


    path = "./images/1.jpeg"
    my_image = Image.open(path)
    my_image = my_image.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(my_image)
    panel = tk.Label(window, image = img)
    panel.pack()

    button = tk.Button(text="Click this button to see another cat!",
        width=30,
        height=3,
        fg="black",
        command=lambda: next_image(panel)
    )
    button.pack()

    window.mainloop()

if __name__ == '__main__':
    user_interface()
