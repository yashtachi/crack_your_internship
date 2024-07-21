#User function Template for python3

class TwoStacks:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push1(self, x):
        self.s1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.s2.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        return self.s1.pop() if self.s1 else -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        return self.s2.pop() if self.s2 else -1