# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        results = []
        record = []
        self.dfs(results, root, target, record)
        return results

    def dfs(self, results, root, target, record):
        if not root:
            return
        record.append(root.val)
        if not root.left and not root.right and target == root.val:
            results.append([_ for _ in record])
        else:
            target -= root.val
            self.dfs(results, root.left, target, record)
            self.dfs(results, root.right, target, record)
        record.pop()
