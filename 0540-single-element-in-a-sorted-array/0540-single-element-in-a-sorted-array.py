class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        while left<right:
            mid=int((right-left)//2) + left
            if  nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif (mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2!=0 and nums[mid]==nums[mid+1]):
                right=mid-1
            else:
                left=mid+1
            
        
        return nums[left]        
         
            