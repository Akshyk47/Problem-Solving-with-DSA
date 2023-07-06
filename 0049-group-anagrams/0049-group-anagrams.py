class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}        
        for s in strs:
	        count = [0]*26
	        for c in s:
		        count[ord(c)-ord('a')] += 1
	        count = tuple(count)
	        hm[count] = [s]+hm.get(count, [])
	
        return hm.values()
        