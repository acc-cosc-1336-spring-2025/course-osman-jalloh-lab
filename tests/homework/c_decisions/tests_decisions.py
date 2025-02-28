import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        # Test that get_options_ratio with values 5 and 20 returns 0.25
        self.assertEqual(get_options_ratio(5, 20), 0.25)
        # Test that get_options_ratio with values 10 and 20 returns 0.5
        self.assertEqual(get_options_ratio(10, 20), 0.5)

    def test_get_faculty_rating(self):
        # Test ratings based on ratios
        self.assertEqual(get_faculty_rating(0.91), 'Excellent')
        self.assertEqual(get_faculty_rating(0.85), 'Very Good')
        self.assertEqual(get_faculty_rating(0.71), 'Good')
        self.assertEqual(get_faculty_rating(0.66), 'Needs Improvement')
        self.assertEqual(get_faculty_rating(0.45), 'Unacceptable')

if __name__ == '__main__':
    unittest.main()
