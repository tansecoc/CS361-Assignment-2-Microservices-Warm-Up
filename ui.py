import tkinter as tk
from PIL import ImageTk, Image
import time

def call_prng():
    f = open('prng-service.txt', "w")
    f.write('run')
    f.close()
    time.sleep(.02)
    
    f = open('prng-service.txt', "r")
    random_number = f.read()
    f.close()

    f = open('prng-service.txt', "w")
    f.write('')
    f.close()

    return random_number

def call_image_service(random_number):
    f = open('image-service.txt', "w")
    f.write(str(random_number))
    f.close()
    time.sleep(.02)
    
    f = open('image-service.txt', "r")
    path = f.read()
    f.close()

    f = open('image-service.txt', "w")
    f.write('')
    f.close()

    return path

def next_image(panel):
    random_number = call_prng()
    path = call_image_service(random_number)

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
