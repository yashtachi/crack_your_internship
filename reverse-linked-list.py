class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev =None
        if head == None or head.next==None:
            return head
        n=head.next
        while n!=None:
            head.next=prev
            prev=head
            head=n
            n=n.next
        head.next=prev
        prev=head
        head=n
        return prev
