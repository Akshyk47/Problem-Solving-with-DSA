class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = {}

        for n in nums:
            if n in hashset:
                return True
            hashset[n]=hashset.get(n,0)+1
        return False