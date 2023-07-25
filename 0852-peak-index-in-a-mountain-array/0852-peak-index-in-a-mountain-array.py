class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left=0
        right=len(arr)-1
        
        while left<right:
            mid=right+left//2
            
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif mid-1>-1 and arr[mid-1]<arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                right=mid-1
                
        return left
        