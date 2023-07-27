class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        batteries.sort()
        energy= sum(batteries)
        while batteries[-1] > energy/ n:
            n -= 1
            energy-= batteries.pop()
        return energy // n
        