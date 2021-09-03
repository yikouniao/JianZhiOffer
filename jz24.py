# https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p1, p2 = head, head.next
        p1.next = None
        while p2:
            t = p2.next
            p2.next = p1
            p1 = p2
            p2 = t
        return p1
