# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

class Solution:
    def permutation(self, s: str) -> List[str]:
        arr = list(s)
        results = set()
        n = len(arr)
        flag = [False] * n
        res = ""
        self.dfs(flag, results, n, arr, res)
        return list(results)
        
    def dfs(self, flag, results, n, arr, res):
        if len(res) == n:
            results.add(res)
            return
        for i in range(len(flag)):
            if not flag[i]:
                res += arr[i]
                flag[i] = True
                self.dfs(flag, results, n, arr, res)
                flag[i] = False
                res = res[:-1]
