class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        if head is  None :
            return head
        b = ListNode(0)
        b.next=head
        c=b
        a=head
        while a is not None :
            if a.next is not None and a.val == a.next.val:
                a=a.next
            else:
                c.next=a
                c=c.next
                a=a.next
        c.next=None
        return b.next