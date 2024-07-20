class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        if not head:
            return head
        d=ListNode(None)
        l=d
        l.next=head
        while l.next:
            if l.next.val==val:
                l.next=l.next.next
            else:
                l=l.next
            
        return d.next