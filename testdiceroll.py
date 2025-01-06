import unittest
import random

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

if __name__ == "__main__":
    unittest.main()
