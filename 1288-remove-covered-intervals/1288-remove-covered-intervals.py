class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i : (i[0],-i[1]))
        
        result=[intervals[0]]
        
        for start,end in intervals[1:]:
            prevStart,prevEnd=result[-1]
            
            if prevStart<=start and prevEnd>=end:
                continue
            result.append([start,end])
            
        return len(result)
            
        
            
        