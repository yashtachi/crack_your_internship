class Solution:
    def findPair(self, n : int, x : int, arr ) -> int:
        d={}
        for i in arr:
            if i-x in d or i+x in d :
                return 1
            d.setdefault(i,0)
            d[i]+=1
        return -1