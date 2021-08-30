# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        p = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:p + 1], inorder[:p])
        root.right = self.buildTree(preorder[p + 1:], inorder[p + 1:])
        return root
