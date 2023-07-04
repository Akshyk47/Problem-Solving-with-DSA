class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freqcount_s={}
        freqcount_t={}
        for c in s:
            freqcount_s[c]=freqcount_s.get(c,0)+1
        for c in t:
            freqcount_t[c]=freqcount_t.get(c,0)+1
        for c in s:
            if freqcount_s[c]!=freqcount_t.get(c,0):
                return False
        return True
        
        