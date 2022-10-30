import unittest

from leetcode.problem_2455 import Solution


class SolutionTest(unittest.TestCase):

    def test_averageValue(self):
        self.assertEqual(Solution().averageValue([1, 3, 6, 10, 12, 15]), 9)
        self.assertEqual(Solution().averageValue([1, 2, 4, 7, 10]), 0)

