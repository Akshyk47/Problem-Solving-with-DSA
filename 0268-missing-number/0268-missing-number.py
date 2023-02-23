class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=0
        
        for index in range(len(nums)):
            result=result^index+1^nums[index]
        return result
        