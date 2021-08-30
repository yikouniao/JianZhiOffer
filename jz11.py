# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if n == 0:
            return -1
        p, q, i = 0, n - 1, 0
        while p < q:
            i = (p + q) // 2
            if numbers[i] > numbers[q]:
                p = i + 1
            elif numbers[i] < numbers[q]:
                q = i
            else:
                q -= 1
        return numbers[p]
