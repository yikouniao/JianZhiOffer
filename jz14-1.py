# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

class Solution:
    def cuttingRope(self, n: int) -> int:
        table = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                table[i] = max(table[j] * (i - j), j * (i - j), table[i])
        return table[n]
