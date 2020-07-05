class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dynamic programming solution
        memo = [-1 for _ in range(amount + 1)]
        memo[0] = 0
        for i in range(len(memo)):
            for coin in coins:
                if i - coin >= 0 and memo[i - coin] != -1:
                    if memo[i] == -1:
                        memo[i] = memo[i - coin] + 1
                    else:
                        memo[i] = min(memo[i - coin] + 1, memo[i])
        return memo[-1]
