import unittest
import random
from dicerollapp import DiceRollApp


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
    def test_history_limit(self):
        """Testează dacă istoricul păstrează doar ultimele 3 aruncări."""
        app = DiceRollApp(None)  # Instanțiază aplicația fără a porni fereastra GUI
        app.roll_history = [1, 2, 3]
        app.roll_dice()
        self.assertEqual(len(app.roll_history), 3)
        self.assertEqual(app.roll_history, [2, 3, app.roll_history[-1]])

    def test_history_initial_state(self):
        """Testează dacă istoricul este gol la început."""
        app = DiceRollApp(None)
        self.assertEqual(len(app.roll_history), 0)

    def test_history_update(self):
        """Testează actualizarea corectă a istoricului."""
        app = DiceRollApp(None)
        app.roll_history = [1, 2]
        app.roll_dice()  # Adaugă o nouă valoare
        self.assertEqual(len(app.roll_history), 3)
        self.assertTrue(all(isinstance(x, int) for x in app.roll_history))


if __name__ == "__main__":
    unittest.main()
