class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(','}':'{',']':'['}
        n=len(s)
        stack.append(s[0])
        for i in range(1,n):
            if s[i] in d and len(stack):
                if stack[-1]==d[s[i]]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return len(stack)==0
