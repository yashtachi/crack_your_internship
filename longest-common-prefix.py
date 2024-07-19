class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans=''
        v=sorted(strs)
        f=v[0]
        l=v[-1]
        for i in range(min(len(f),len(l))):
            if(f[i]!=l[i]):
                return ans
            ans+=f[i]
        return ans