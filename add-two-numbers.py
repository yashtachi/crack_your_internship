class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        t1=l1
        t2=l2
        dummy=ListNode(-1)
        temp=dummy
        c=0
        while t1 and t2:
            s=t1.val + t2.val + c
            c=s//10
            dummy.next=ListNode(s%10)
            t1=t1.next
            t2=t2.next
            dummy=dummy.next
        while t1:
            s=t1.val + c
            c=s//10
            dummy.next=ListNode(s%10)
            dummy=dummy.next
            t1=t1.next
        while t2:
            s=t2.val + c
            c=s//10
            dummy.next=ListNode(s%10)
            dummy=dummy.next
            t2=t2.next
        if c>0:
            dummy.next=ListNode(c)   
        return temp.next