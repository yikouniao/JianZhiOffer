# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        for _ in range(1, k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1
