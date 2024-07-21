class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l.sort()
        nh=ListNode(None)
        t=nh
        for i in l:
            t.next=ListNode(i)
            t=t.next
        return nh.next