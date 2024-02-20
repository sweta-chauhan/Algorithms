import unittest

from src.algorithms.greedy_algorithms.coin_change import CoinChangeFactory, CoinChangeMethod


class TestCoinChangeFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.target = 4
        self.coins = [1, 2, 3]
        self.number_of_coins = 3

    def test_brute_force_method(self):
        coin_change_factory = CoinChangeFactory(
            self.target,
            self.coins, self.number_of_coins,
            CoinChangeMethod.BRUTE_FORCE
        )
        assert coin_change_factory.count() == 4

    def test_greedy_method(self):
        coin_change_factory = CoinChangeFactory(
            self.target,
            self.coins, self.number_of_coins,
            CoinChangeMethod.GREEDY
        )
        assert coin_change_factory.count() == 4

    def test_dynamic_tabulation_method(self):
        coin_change_factory = CoinChangeFactory(
            self.target,
            self.coins, self.number_of_coins,
            CoinChangeMethod.DYNAMIC_TABULATION_SPC_OPTIMISED
        )
        assert coin_change_factory.count() == 4

    def test_dynamic_tabulation_spc_method(self):
        coin_change_factory = CoinChangeFactory(
            self.target,
            self.coins, self.number_of_coins,
            CoinChangeMethod.DYNAMIC_TABULATION
        )
        assert coin_change_factory.count() == 4

    def test_dynamic_memoization_method(self):
        coin_change_factory = CoinChangeFactory(
                self.target,
                self.coins, self.number_of_coins,
                CoinChangeMethod.DYNAMIC_MEMOIZATION
        )
        assert coin_change_factory.count() == 4
