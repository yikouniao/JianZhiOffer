# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n, m = len(pushed), len(popped)
        if n != m:
            return False
        if n == 0:
            return True
        stack = []
        p = 0
        for e in pushed:
            stack.append(e)
            while len(stack) > 0 and p < n and stack[-1] == popped[p]:
                p += 1
                stack.pop()

        return p == n
