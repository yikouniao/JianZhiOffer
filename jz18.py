# https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        limit = 0
        while n > 0:
            limit = limit * 10 + 9
            n -= 1
        return [_ for _ in range(1, limit + 1)]
