class Solution:
    def maxProduct(self, nums) -> int:
        p = 0
        n = 0
        flag = False
        ans = -float('inf')
        
        for x in nums:
            if x == 0:
                p = 0
                n = 0
                flag = False
            
            elif x > 0:
                
                if p == 0:
                    p = x   
                else:
                    p *= x
                    if p < 0:
                        p //= n
                        flag = True
            else:
                p = p * x if p != 0 else x
                if p < 0:
                    if n == 0:
                        n = p
                    elif flag:
                        p *= n
                        flag = False
                    
                    else:
                        p //= n
                        flag = True
            if p > ans:
                ans = p
        
        return ans