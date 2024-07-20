class node:
    def __init__(self):
        self.data = None
        self.next = None
M = 10**9+7
class Solution:
    def multiply_two_lists(self, first, second):
        s1,s2=0,0
        while first:
            s1 = (s1*10 + (first.data))%M
            first=first.next
        while second:
            s2= (s2*10 + (second.data))%M
            second=second.next
        return ((s1)*(s2)) % M