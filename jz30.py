# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elem = []
        self.elem_min = []


    def push(self, x: int) -> None:
        self.elem.append(x)
        if len(self.elem_min) == 0:
            self.elem_min.append(x)
        else:
            self.elem_min.append(min(x, self.elem_min[-1]))
            

    def pop(self) -> None:
        _ = self.elem.pop()
        _ = self.elem_min.pop()

    def top(self) -> int:
        return self.elem[-1]

    def min(self) -> int:
        return self.elem_min[-1]
