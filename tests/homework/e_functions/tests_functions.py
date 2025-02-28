import unittest
from src.homework.e_functions.value_return import get_hours
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds

class Test_Config(unittest.TestCase):

    def test_get_hours(self):
        self.assertEqual(get_hours(3800), 1)  # 3800 seconds -> 1 hour
        self.assertEqual(get_hours(3600), 1)  # 3600 seconds -> 1 hour
        self.assertEqual(get_hours(86400), 0)  # 86400 seconds -> 0 hours (24 hours)

    def test_get_minutes(self):
        self.assertEqual(get_minutes(3800), 3)  # 3800 seconds -> 3 minutes (since 3800 = 1 hour + 3 minutes)
        self.assertEqual(get_minutes(3600), 0)  # 3600 seconds -> 0 minutes (exactly 1 hour, no extra minutes)
        self.assertEqual(get_minutes(3661), 1)  # 3661 seconds -> 1 minute (1 hour 1 minute 1 second)

    def test_get_seconds(self):
        self.assertEqual(get_seconds(3800), 20)  # 3800 seconds -> 20 seconds (since 3800 = 1 hour + 3 minutes + 20 seconds)
        self.assertEqual(get_seconds(3600), 0)  # 3600 seconds -> 0 seconds (exactly 1 hour)
        self.assertEqual(get_seconds(3661), 1)  # 3661 seconds -> 1 second (1 hour 1 minute 1 second)

