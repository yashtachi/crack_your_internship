class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        d={}
        if head==None or head.next==None:
            return False
        while head:
            if head in d:
                return True
            d.setdefault(head,0)
            head=head.next
        return False
        