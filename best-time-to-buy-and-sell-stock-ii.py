class Solution:
    def maxProfit(self, prices) -> int:
        n=len(prices)
        ans=0
        p1,p2=0,1
        while p2<n and p1<p2:
            if prices[p1]>prices[p2]:
                p1+=1
                p2=p1+1
            else:
                ans+=prices[p2]-prices[p1]
                p1+=1
                p2+=1
        return ans