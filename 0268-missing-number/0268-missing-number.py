class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum=sum(range(len(nums)+1))
        given_sum=sum(nums)
        return actual_sum-given_sum
            
        
        