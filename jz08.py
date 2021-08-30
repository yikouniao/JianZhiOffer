# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

class CQueue:
    
    def __init__(self):
        self.s1, self.s2 = [], []

    def appendTail(self, value: int) -> None:
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
        self.s1.append(value)

    def deleteHead(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else -1
