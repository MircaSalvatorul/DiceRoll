import tkinter as tk
from PIL import Image, ImageTk
import random
import os


class DiceRollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll App")
        self.root.geometry("900x900")

        self.title_label = tk.Label(root, text="Dă cu zarul!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.roll_button = tk.Button(root, text="Rulare zar", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack(pady=20)

        self.dice_image_label = tk.Label(root)
        self.dice_image_label.pack(pady=10)

        self.dice_images = [
            ImageTk.PhotoImage(Image.open(os.path.join("images", f"dice_{i}.png"))) for i in range(1, 7)
        ]

        self.dice_images_small = [
            ImageTk.PhotoImage(Image.open(os.path.join("images", f"dice_{i}.png")).resize((30, 30))) for i in range(1, 7)
        ]

        self.roll_history = []

        self.history_frame = tk.Frame(root)
        self.history_frame.pack(pady=20)

    def roll_dice(self):
        dice_result = random.randint(1, 6)
        self.dice_image_label.config(image=self.dice_images[dice_result - 1])

        self.roll_history.append(dice_result)

        if len(self.roll_history) > 3:
            self.roll_history.pop(0)

        for widget in self.history_frame.winfo_children():
            widget.destroy()  # Curățăm frame-ul

        for roll in self.roll_history:
            img_label = tk.Label(self.history_frame, image=self.dice_images_small[roll - 1])
            img_label.pack(side=tk.LEFT, padx=5)
