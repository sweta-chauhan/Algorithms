from abc import ABC, abstractmethod


class CoinChangeMethod:
    BRUTE_FORCE = "brute_force"
    DYNAMIC_MEMOIZATION = "dynamic_memoization"
    DYNAMIC_TABULATION = "dynamic_tabulation"
    DYNAMIC_TABULATION_SPC_OPTIMISED = "dynamic_tabulation_space_optimised"
    GREEDY = "greedy"


class CoinChangeInterface(ABC):
    @abstractmethod
    def count_coins(self, target, coins, number_of_coins):
        pass


class BruteForceCoinChange(CoinChangeInterface):
    def __init__(self):
        pass

    def count_coins(self, target, coins, number_of_coins):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if number_of_coins <= 0:
            return 0

        return (
                self.count_coins(target, coins, number_of_coins - 1) +
                self.count_coins(target - coins[number_of_coins - 1], coins, number_of_coins)
        )


class DynamicProgrammingMCoinChange(CoinChangeInterface):
    def __init__(self):
        pass

    def count_coins(self, target, coins, number_of_coins):
        dp = [[-1 for _ in range(target+1)] for _ in range(number_of_coins+1)]
        return self.count_coins_helper(target, coins, number_of_coins, dp)

    def count_coins_helper(self, target, coins, number_of_coins, dp):
        if target == 0:
            dp[number_of_coins][target] = 1
            return dp[number_of_coins][target]
        if (
                (number_of_coins <= 0) or
                (target < 0)
        ):
            return 0

        dp[number_of_coins][target] = (
                self.count_coins_helper(target, coins, number_of_coins-1, dp) +
                self.count_coins_helper(target-coins[number_of_coins-1], coins, number_of_coins, dp)
        )
        return dp[number_of_coins][target]


class DynamicProgrammingTCoinChange(CoinChangeInterface):
    def __init__(self):
        pass

    def count_coins(self, target, coins, number_of_coins):
        dp = [[0 for _ in range(target+1)] for _ in range(number_of_coins+1)]
        dp[0][0] = 1
        for coin in range(1, number_of_coins+1):
            for target_sum in range(target+1):
                dp[coin][target_sum] += dp[coin-1][target_sum]

                if (target_sum - coins[coin-1]) >= 0:
                    dp[coin][target_sum] += dp[coin][target_sum-coins[coin-1]]

        return dp[number_of_coins][target]


class DynamicProgrammingTIICoinChange(CoinChangeInterface):
    def __init__(self):
        pass

    def count_coins(self, target, coins, number_of_coins):
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for coin in range(number_of_coins):
            for target_sum in range(coins[coin], target+1):
                dp[target_sum] += dp[target_sum-coins[coin]]

        return dp[target]


class GreedyCoinChange(CoinChangeInterface):
    def __init__(self):
        pass

    def count_coins(self, target, coins, number_of_coins):
        coins = sorted(coins)
        count, ans = 0, []
        for coin_index in range(number_of_coins):
            while target >= coins[coin_index]:
                target -= coins[coin_index]
                ans.append(coins[coin_index])
                count += 1
        return count


class CoinChangeFactory:
    def __init__(self, target, coins, number_of_coins, method):
        self.method = method
        self.number_of_coins = number_of_coins
        self.coins = coins
        self.target = target

    def set_method(self, method):
        self.method = method

    def count(self):
        if self.method == CoinChangeMethod.BRUTE_FORCE:
            return BruteForceCoinChange().count_coins(self.target, self.coins, self.number_of_coins)

        elif self.method == CoinChangeMethod.DYNAMIC_MEMOIZATION:
            return DynamicProgrammingMCoinChange().count_coins(self.target, self.coins, self.number_of_coins)

        elif self.method == CoinChangeMethod.DYNAMIC_TABULATION:
            return DynamicProgrammingTCoinChange().count_coins(self.target, self.coins, self.number_of_coins)

        elif self.method == CoinChangeMethod.DYNAMIC_TABULATION_SPC_OPTIMISED:
            return DynamicProgrammingTIICoinChange().count_coins(self.target, self.coins, self.number_of_coins)

        elif self.method == CoinChangeMethod.GREEDY:
            return GreedyCoinChange().count_coins(self.target, self.coins, self.number_of_coins)

        else:
            raise("NotImplemented")




