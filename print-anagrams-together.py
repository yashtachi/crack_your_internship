class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        d={}
        for i in words:
            t = ''.join(sorted(i))
            d.setdefault(t,[])
            d[t].append(i)
        return list(d.values())