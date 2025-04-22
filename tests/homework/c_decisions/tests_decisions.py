# In tests/homework/c_decisions/test_decisions.py

import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        # Test case for the ratio function
        self.assertEqual(get_options_ratio(5, 20), 0.25)  # 5/20 should return 0.25
        self.assertEqual(get_options_ratio(10, 20), 0.5)  # 10/20 should return 0.5

    def test_get_faculty_rating(self):
        # Test case for the rating function based on ratio
        self.assertEqual(get_faculty_rating(0.91), "Excellent")
        self.assertEqual(get_faculty_rating(0.85), "Very Good")
        self.assertEqual(get_faculty_rating(0.71), "Good")
        self.assertEqual(get_faculty_rating(0.66), "Needs Improvement")
        self.assertEqual(get_faculty_rating(0.45), "Unacceptable")

if __name__ == "__main__":
    unittest.main()


