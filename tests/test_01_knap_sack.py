import unittest

from src.algorithms.dynamic_programming.knap_sack_0_1 import recursive_01_knap_sack, memoized_01_knap_sack_helper, \
    tabulated_01_knap_sack


class Test01KnapSack(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [60, 100, 120]
        self.weights = [10, 20, 30]
        self.capacity = 50
        self.number_of_weights = 3

    def test_recursive_01_knap_sack(self):
        result = recursive_01_knap_sack(
            capacity=self.capacity,
            weights=self.weights,
            profits=self.values,
            number_of_weights=self.number_of_weights
        )

        assert result == 220

    def test_memoized_01_knap_sack_helper(self):
        result1 = memoized_01_knap_sack_helper(
            capacity=self.capacity,
            weights=self.weights,
            profits=self.values,
            number_of_weights=self.number_of_weights
        )

        return result1 == 220

    def test_tabulated_01_knap_sack(self):
        result2 = tabulated_01_knap_sack(
            capacity=self.capacity,
            weights=self.weights,
            profits=self.values,
            number_of_weights=self.number_of_weights
        )

        assert result2 == 220
