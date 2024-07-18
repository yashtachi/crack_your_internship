class Solution:
    def maxProfit(self, prices) -> int:
        ans=0
        m=100001
        for i in prices:
            m=min(i,m)
            ans=max(ans,i-m)
        return ans