# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

class Solution:
    def fib(self, n: int) -> int:
        table = [0, 1]
        if n < 2:
            return table[n]
        for i in range(2, n + 1):
            table.append(table[-1] + table[-2])
        return table[-1] % 1000000007
