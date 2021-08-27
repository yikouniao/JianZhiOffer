# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next
        return l[::-1]
