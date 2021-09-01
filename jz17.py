# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            if n % 2:
                t = self.myPow(x, n // 2)
                return t * t * x
            else:
                t = self.myPow(x, n // 2)
                return t * t
