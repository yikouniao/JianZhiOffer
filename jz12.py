# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0:
            return False
        m = len(board[0])
        if m == 0:
            return False
        
        flag = [[False] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                r = self.dfs(i, j, n, m, flag, board, word, 0)
                if r:
                    return True
        return False
    
    def dfs(self, i, j, n, m, flag, board, word, p):
        if i < 0 or j < 0 or i >= n or j >= m or flag[i][j] or word[p] != board[i][j]:
            return False
        if p == len(word) - 1:
            return True
        flag[i][j] = True
        r = self.dfs(i, j + 1, n, m, flag, board, word, p + 1) or \
            self.dfs(i, j - 1, n, m, flag, board, word, p + 1) or \
            self.dfs(i + 1, j, n, m, flag, board, word, p + 1) or \
            self.dfs(i - 1, j, n, m, flag, board, word, p + 1)
        if not r:
            flag[i][j] = False
        return r
