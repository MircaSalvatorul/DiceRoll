import tkinter as tk
from PIL import Image, ImageTk
import random
import os


class DiceRollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll App - Doi Jucători")
        self.root.geometry("900x900")

        self.title_label = tk.Label(root, text="Dă cu zarul!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Cadru pentru butoane si istoricul jucatorilor
        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(fill=tk.X, pady=10)

        # Buton si istoric Jucator 1
        self.player1_frame = tk.Frame(self.controls_frame)
        self.player1_frame.pack(side=tk.LEFT, padx=20)

        self.player1_button = tk.Button(self.player1_frame, text="Rulare zar Jucator 1", font=("Arial", 14), command=lambda: self.roll_dice("Jucător 1"))
        self.player1_button.pack()

        self.player1_history_frame = tk.Frame(self.player1_frame)
        self.player1_history_frame.pack(pady=5)

        self.player1_history = []

        # Buton și istoric Jucator 2
        self.player2_frame = tk.Frame(self.controls_frame)
        self.player2_frame.pack(side=tk.RIGHT, padx=20)

        self.player2_button = tk.Button(self.player2_frame, text="Rulare zar Jucator 2", font=("Arial", 14), command=lambda: self.roll_dice("Jucător 2"))
        self.player2_button.pack()

        self.player2_history_frame = tk.Frame(self.player2_frame)
        self.player2_history_frame.pack(pady=5)

        self.player2_history = []

        # Cadru pentru zar
        self.dice_frame = tk.Frame(root)
        self.dice_frame.pack(pady=20)

        self.dice_image_label = tk.Label(self.dice_frame)
        self.dice_image_label.pack()

        # Încarcare imagini zaruri
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(os.path.join("images", f"dice_{i}.png")).resize((300,300))) for i in range(1, 7)
        ]

        self.dice_images_small = [
            ImageTk.PhotoImage(Image.open(os.path.join("images", f"dice_{i}.png")).resize((30, 30))) for i in range(1, 7)
        ]


    def roll_dice(self, player):
        dice_result = random.randint(1, 6)
        self.dice_image_label.config(image=self.dice_images[dice_result - 1])

        if player == "Jucător 1":
            self.update_history(self.player1_history, self.player1_history_frame, dice_result)
        elif player == "Jucător 2":
            self.update_history(self.player2_history, self.player2_history_frame, dice_result)

    def update_history(self, history, history_frame, dice_result):
        history.append(dice_result)
        if len(history) > 5:
            history.pop(0)

        for widget in history_frame.winfo_children():
            widget.destroy()

        for roll in history:
            img_label = tk.Label(history_frame, image=self.dice_images_small[roll - 1])
            img_label.pack(side=tk.TOP, pady=2)
