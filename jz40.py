# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        result = []
        max_p = 0
        for a in arr:
            if len(result) < k:
                result.append(a)
                if result[max_p] < result[-1]:
                    max_p = len(result) - 1
            elif result[max_p] > a:
                result[max_p] = a
                for i in range(k):
                    if result[i] > result[max_p]:
                        max_p = i
        return result
