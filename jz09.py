# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n < 2:
            return n
        for i in range(2, n + 1):
            a, b = b, (a + b) % 1000000007
        return b
