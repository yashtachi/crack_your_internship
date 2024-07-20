class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def length(h):
    c=-1
    while h:
        c+=1
        h=h.next
    return c
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        d=head
        l=length(head)
        i=0
        if l==0:
            if head.val==1:
                return 1
            else:
                return 0
        while d:
            if d.val==1:
                i+=(1<<l)
            l-=1
            d=d.next
        return i