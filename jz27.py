# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root
