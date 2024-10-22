class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def middleNode(self, head):
        if not head:
            return head
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow