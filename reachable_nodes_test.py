import unittest
from reachable_nodes import reachables

class TestReachableNodes(unittest.TestCase):
    def test_returned_value(self):
        self.assertEqual(reachables([[1, 3], [2], [0], [4], [3], []], 3), {3, 4})
        self.assertEqual(reachables([[1, 3], [2], [0], [4], [3], []], 0), {0, 1, 2, 3, 4})

    def test_input_value(self):
        self.assertRaises(IndexError, reachables, [], True)
        self.assertRaises(IndexError, reachables, [[1, 3], [2], [0], [4], [3], []], 20)
        self.assertRaises(TypeError, reachables, None, None)
        self.assertRaises(TypeError, reachables)
