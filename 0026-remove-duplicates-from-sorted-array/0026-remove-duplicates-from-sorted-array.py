class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        while right<len(nums):
            if nums[left]!=nums[right]:
                nums[left+1]=nums[right]
                left=left+1
            right=right+1
            
        return left+1
            
        
"""
The logic is to put the unique k elements by comparing the left with right and putting the unequal right num to the right of the left num and continously incremet right until a next unique element is found to put it to the next right and the as we need the value k the position at which the left stops+ 1 is the k
"""
        