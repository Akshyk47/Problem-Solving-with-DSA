class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==1 or len(nums)==0:
            return False
        freq_map={}
        #Create the freq table
        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1
        
        #iterate over the hashmap and check if any ke maps to value greater than 1
        for key in freq_map:
            if freq_map[key]>1:
                return True
            
        #if the loop terminates it means all numbers are distinct 
        return False
        
      
        