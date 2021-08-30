# https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/

class Solution:
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, (a + b) % 1000000007
        return b
