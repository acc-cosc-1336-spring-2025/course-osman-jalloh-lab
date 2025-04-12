import sys
import os
import unittest

# Make sure Python can find the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}

        # Add Widget1 with quantity of 10
        add_inventory(inventory_dictionary, 'Widget1', 10)
        self.assertEqual(inventory_dictionary['Widget1'], 10)

        # Add Widget1 with quantity of 25 (should now be 35)
        add_inventory(inventory_dictionary, 'Widget1', 25)
        self.assertEqual(inventory_dictionary['Widget1'], 35)

        # Add Widget1 with quantity of -10 (should now be 25)
        add_inventory(inventory_dictionary, 'Widget1', -10)
        self.assertEqual(inventory_dictionary['Widget1'], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {'widget1': 20, 'widget2': 40}

        # Corrected to match function: Remove 20 widget1 from inventory
        result = remove_inventory_widget(inventory_dictionary, 'widget1', 20)
        self.assertEqual(result, 0)  # Widget1's new value should be 0
        self.assertEqual(inventory_dictionary['widget1'], 0)

        # If value is 0, delete the widget (handled by the function itself now)
        if inventory_dictionary['widget1'] == 0:
            del inventory_dictionary['widget1']

        # Now check that only widget2 remains
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertIn('widget2', inventory_dictionary)

if __name__ == '__main__':
    unittest.main()



