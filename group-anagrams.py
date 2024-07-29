class Solution:
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            t = ''.join(sorted(i))
            d.setdefault(t,[])
            d[t].append(i)
        return list(d.values())

