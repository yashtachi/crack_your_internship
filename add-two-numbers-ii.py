class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        n1,n2=0,0
        while l1:
            n1 = n1 * 10 + l1.val
            l1=l1.next
        while l2:
            n2 = n2 *10 + l2.val
            l2=l2.next
        n=str(n1+n2)
        h=ListNode(None)
        l=h
        for i in n:
            h.next=ListNode(int(i))
            h=h.next
        return l.next