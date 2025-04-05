import unittest
import os
import sys

# Fix the directory path in sys.path.append
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import the functions to test
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix


class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        list1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        list2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
        
        # Test the p-distance between two lists
        self.assertAlmostEqual(get_p_distance(list1, list2), 0.4, places=5)

    def test_get_p_distance_matrix(self):
        sequences = [
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
            ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
            ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        
        # Test the p-distance matrix for multiple sequences
        result = get_p_distance_matrix(sequences)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertAlmostEqual(result[i][j], expected[i][j], places=5)

if __name__ == '__main__':
    unittest.main()


