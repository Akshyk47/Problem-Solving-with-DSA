class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq_map={}
        
        for character in s:
            
            freq_map[character]=freq_map.get(character,0)+1
        
        for index,character in enumerate(s):
            
            if freq_map[character]==1:
                
                return index
        
        return -1
            
        