class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        index=1
        common_set=list(words[0])
        while index<len(words):
            
            com_array=[]
            
            for char in words[index]:
                if char in common_set:
                    com_array.append(char)
                    common_set.remove(char)
            common_set=com_array
            
            index+=1
            
        return com_array
            
        