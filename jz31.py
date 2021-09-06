# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        if n == 0:
            return True
        stack = []
        p_pushed, p_popped = 0, 0
        while p_pushed < n and p_popped < n:
            if len(stack) > 0 and p_popped < n and stack[-1] == popped[p_popped]:
                stack.pop()
                p_popped += 1
            elif pushed[p_pushed] == popped[p_popped]:
                p_pushed, p_popped = p_pushed + 1, p_popped + 1
            else:
                stack.append(pushed[p_pushed])
                p_pushed += 1
        if p_popped < n:
            p_stack = len(stack) - 1
            while p_stack >= 0 and p_popped < n:
                if stack[p_stack] != popped[p_popped]:
                    return False
                else:
                    p_stack, p_popped = p_stack - 1, p_popped + 1
        return True
