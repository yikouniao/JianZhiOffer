# https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        p = ListNode(0)
        p0 = p
        while p1 and p2:
            while p1 and p2 and p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            while p1 and p2 and p1.val > p2.val:
                p.next = p2
                p2 = p2.next
                p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return p0.next
