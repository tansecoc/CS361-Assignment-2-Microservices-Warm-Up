import tkinter as tk
from prng import random_generator

def user_interface():
    window = tk.Tk()

    greeting = tk.Label(text="Welcome to the random image generator.")
    greeting.pack()

    button = tk.Button(text="Click me!",
        width=10,
        height=2,
        fg="black"
    )
    button.pack()

    def handle_click(event):
        random_number = random_generator()
        print(random_number)

    button.bind("<Button-1>", handle_click)

    window.mainloop()

if __name__ == '__main__':
    user_interface()
