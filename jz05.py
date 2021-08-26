# https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

class Solution:
    def replaceSpace(self, s: str) -> str:
        origin_len = len(s)
        space_cnt = 0
        for c in s:
            if c == ' ':
                space_cnt += 1
        l = list(s) + ['C'] * (space_cnt * 2)
        p, q = origin_len - 1, len(l) - 1
        while p >= 0:
            if l[p] != ' ':
                l[q] = l[p]
                p -= 1
                q -= 1
            else:
                l[q - 2], l[q - 1], l[q] = '%', '2', '0'
                p -= 1
                q -= 3
        return ''.join(l)
