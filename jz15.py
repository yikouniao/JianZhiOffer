# https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        return dp[n] % 1000000007
