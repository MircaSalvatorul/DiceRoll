import unittest
import random
from dicerollapp import DiceRollApp
import tkinter as tk
import os
from PIL import Image

class TestDiceRollLogic(unittest.TestCase):
    def test_roll_dice_valid_range(self):
        """Testeaza daca zarul genereaza valori intre 1 și 6."""
        for _ in range(1000):
            result = random.randint(1, 6)
            self.assertIn(result, range(1, 7))

    def test_roll_dice_randomness(self):
        """Testeaza distributia aproximativ uniforma a zarurilor."""
        results = [random.randint(1, 6) for _ in range(10000)]
        counts = {i: results.count(i) for i in range(1, 7)}
        for count in counts.values():
            self.assertTrue(abs(count - 1667) < 500, "Distribuția nu este uniformă")


class TestDiceRollHistory(unittest.TestCase):
    def setUp(self):
        """Seteaza aplicatia inainte de fiecare test."""
        self.root = tk.Tk()
        self.app = DiceRollApp(self.root)

    def tearDown(self):
        """Inchide fereastra dupa fiecare test."""
        self.root.destroy()

    def test_history_limit(self):
        """Testeaza daca istoricul pastreaza doar ultimele 3 aruncari."""
        self.app.roll_history = [1, 2, 3]
        self.app.roll_dice()
        self.assertEqual(len(self.app.roll_history), 3)
        self.assertEqual(self.app.roll_history[:-1], [2, 3])

    def test_history_initial_state(self):
        """Testeaza dacă istoricul este gol la inceput."""
        self.assertEqual(len(self.app.roll_history), 0)

    def test_history_update(self):
        """Testeaza actualizarea corecta a istoricului."""
        self.app.roll_history = [1, 2]
        self.app.roll_dice()  # Adauga o noua valoare
        self.assertEqual(len(self.app.roll_history), 3)
        self.assertTrue(all(isinstance(x, int) for x in self.app.roll_history))


class TestDiceImages(unittest.TestCase):
    def test_images_exist(self):
        """Testeaza daca fisierele de imagine exista."""
        for i in range(1, 7):
            path = os.path.join("images", f"dice_{i}.png")
            self.assertTrue(os.path.exists(path), f"Imaginea {path} nu există")

    def test_images_are_valid(self):
        """Testeaza daca fisierele de imagine sunt valide."""
        for i in range(1, 7):
            path = os.path.join("images", f"dice_{i}.png")
            with open(path, "rb") as img_file:
                img = Image.open(img_file)
                img.verify()


class TestDiceGUI(unittest.TestCase):
    """General tkinter functionality"""
    def setUp(self):
        """Configureaza aplicația inainte de fiecare test."""
        self.root = tk.Tk()
        self.app = DiceRollApp(self.root)

    def tearDown(self):
        """Închide fereastra dupa test."""
        self.root.destroy()

    def test_button_text(self):
        """Testeaza textul butonului."""
        self.assertEqual(self.app.roll_button['text'], "Rulare zar")

    def test_title_label_text(self):
        """Testeaza textul etichetei de titlu."""
        self.assertEqual(self.app.title_label['text'], "Dă cu zarul!")

    def test_history_frame_initial_state(self):
        """Testeaza dacă istoricul este gol inițial."""
        self.assertEqual(len(self.app.history_frame.winfo_children()), 0)


if __name__ == "__main__":
    unittest.main()
