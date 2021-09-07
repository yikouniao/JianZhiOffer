# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        n = len(postorder)
        if n < 2:
            return True
        i = 0
        while i < n - 1:
            if postorder[i] < postorder[-1]:
                i += 1
            else:
                break
        if i == n - 1:
            return self.verifyPostorder(postorder[:-1])
        j = i + 1
        while j < n - 1:
            if postorder[j] < postorder[-1]:
                return False
            else:
                j += 1
        return self.verifyPostorder(postorder[:i]) and self.verifyPostorder(postorder[i:-1])
