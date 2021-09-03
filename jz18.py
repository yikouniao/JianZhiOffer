# https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val == val:
            return head.next
        
        p1 = ListNode(0)
        p1.next = head
        p2 = head
        while p2:
            if p2.val == val:
                p1.next = p2.next
                break
            else:
                p1, p2 = p1.next, p2.next
        return head
      
