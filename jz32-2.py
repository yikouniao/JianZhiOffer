# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        queue = [root]
        level = [0]
        while queue:
            p = queue.pop(0)
            l = level.pop(0)
            if len(result) == l:
                result.append([])
            result[l].append(p.val)
            if p.left:
                queue.append(p.left)
                level.append(l + 1)
            if p.right:
                queue.append(p.right)
                level.append(l + 1)
        return result
