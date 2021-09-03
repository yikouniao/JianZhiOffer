# https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)
        
    def dfs(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 and root2:
            return root1.val == root2.val and self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)
        elif not root1 and not root2:
            return True
        else:
            return False
