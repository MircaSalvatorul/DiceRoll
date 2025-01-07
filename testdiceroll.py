import unittest
import random
from dicerollapp import DiceRollApp
import tkinter as tk


class TestDiceRollLogic(unittest.TestCase):
    def test_roll_dice_valid_range(self):
        """Testează dacă zarul generează valori între 1 și 6."""
        for _ in range(1000):
            result = random.randint(1, 6)
            self.assertIn(result, range(1, 7))

    def test_roll_dice_randomness(self):
        """Testează distribuția aproximativ uniformă a zarurilor."""
        results = [random.randint(1, 6) for _ in range(10000)]
        counts = {i: results.count(i) for i in range(1, 7)}
        for count in counts.values():
            self.assertTrue(abs(count - 1667) < 500, "Distribuția nu este uniformă")


class TestDiceRollHistory(unittest.TestCase):
    def setUp(self):
        """Setează aplicația înainte de fiecare test."""
        self.root = tk.Tk()
        self.app = DiceRollApp(self.root)

    def tearDown(self):
        """Închide fereastra după fiecare test."""
        self.root.destroy()

    def test_history_limit(self):
        """Testează dacă istoricul păstrează doar ultimele 3 aruncări."""
        self.app.roll_history = [1, 2, 3]
        self.app.roll_dice()  # Simulează o aruncare
        self.assertEqual(len(self.app.roll_history), 3)
        self.assertEqual(self.app.roll_history[:-1], [2, 3])

    def test_history_initial_state(self):
        """Testează dacă istoricul este gol la început."""
        self.assertEqual(len(self.app.roll_history), 0)

    def test_history_update(self):
        """Testează actualizarea corectă a istoricului."""
        self.app.roll_history = [1, 2]
        self.app.roll_dice()  # Adaugă o nouă valoare
        self.assertEqual(len(self.app.roll_history), 3)
        self.assertTrue(all(isinstance(x, int) for x in self.app.roll_history))


if __name__ == "__main__":
    unittest.main()
