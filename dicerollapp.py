import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import time


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

        # Cadru pentru zaruri
        self.dice_frame = tk.Frame(root)
        self.dice_frame.pack(pady=20)

        self.dice_image_label1 = tk.Label(self.dice_frame)
        self.dice_image_label1.pack(side=tk.TOP, padx=10)

        self.dice_image_label2 = tk.Label(self.dice_frame)
        self.dice_image_label2.pack(side=tk.BOTTOM, padx=10)

        # Încarcare imagini zaruri
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(os.path.join("images", f"dice_{i}.png")).resize((150, 150))) for i in range(1, 7)
        ]

        self.dice_images_small = [
            ImageTk.PhotoImage(Image.open(os.path.join("images", f"dice_{i}.png")).resize((30, 30))) for i in range(1, 7)
        ]

    def roll_dice(self, player):

        for _ in range(20):  #20 de run-uri, 0.1 sec per iteratie
            dice_result1 = random.randint(1, 6)
            dice_result2 = random.randint(1, 6)
            self.dice_image_label1.config(image=self.dice_images[dice_result1 - 1])
            self.dice_image_label2.config(image=self.dice_images[dice_result2 - 1])
            self.root.update()
            time.sleep(0.1)

        if player == "Jucător 1":
            self.update_history(self.player1_history, self.player1_history_frame, dice_result1, dice_result2)
        elif player == "Jucător 2":
            self.update_history(self.player2_history, self.player2_history_frame, dice_result1, dice_result2)

    def update_history(self, history, history_frame, dice_result1, dice_result2):
        history.append((dice_result1, dice_result2))
        if len(history) > 5:
            history.pop(0)

        for widget in history_frame.winfo_children():
            widget.destroy()

        for roll1, roll2 in history:
            frame = tk.Frame(history_frame)
            frame.pack(pady=2)

            img_label1 = tk.Label(frame, image=self.dice_images_small[roll1 - 1])
            img_label1.pack(side=tk.LEFT, padx=2)

            img_label2 = tk.Label(frame, image=self.dice_images_small[roll2 - 1])
            img_label2.pack(side=tk.RIGHT, padx=2)
