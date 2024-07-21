#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        op=['+','-','*','/']
        s=[]
        for i in S:
            if i in op:
                a=s.pop()
                b=s.pop()
                if i=='+':
                    s.append(a+b)
                if i=='*':
                    s.append(a*b)
                if i=='-':
                    s.append(b-a)
                if i=='/':
                    s.append(b//a)
            else:
                s.append(int(i))
        return s[0]
        