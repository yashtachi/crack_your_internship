class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        d={}
        while headA:
            d.setdefault(headA,0)
            headA=headA.next
        while headB:
            if headB in d:
                v=headB.val
                return headB
            headB = headB.next
        return headB