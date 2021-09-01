# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

class Solution:
    def hammingWeight(self, n: int) -> int:
        x = n
        cnt = 0
        while x > 0:
            cnt += x % 2
            x = x // 2
        return cnt
