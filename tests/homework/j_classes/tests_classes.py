import unittest
import os
import sys
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_roll_value_range(self):
        die = Die()
        for _ in range(3):  # Test 3 rolls
            die.roll()
            value = die.get_rolled_value()
            self.assertIn(value, range(1, 7), f"Value {value} not in range 1-6")

