import unittest
from matrix_to_list import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_returned_value(self):
        self.assertEqual(matrix_to_list([[0, 1], [0, 0]]), [[1], []])
        self.assertEqual(matrix_to_list([[], []]), [[], []])
        self.assertEqual(matrix_to_list([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]), [[1], [0, 2, 3], [1], [1]])

    def test_input_value(self):
        self.assertRaises(TypeError, matrix_to_list, 1)
        self.assertRaises(TypeError, matrix_to_list, True)
        self.assertRaises(TypeError, matrix_to_list, { 1, 2 })
