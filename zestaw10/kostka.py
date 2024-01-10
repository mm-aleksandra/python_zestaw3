
import tkinter as tk
import random

def roll_dice():
    dice_result = random.randint(1, 6)
    result_label.config(text=str(dice_result))


root = tk.Tk()
root.title("Dice Simulator")

width = 200
height = 200
root.geometry("{}x{}".format(width, height))

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(padx=10, pady=15) 

result_label = tk.Label(root, text="", font=("times", 36))
result_label.pack(pady=15)

root.mainloop()
