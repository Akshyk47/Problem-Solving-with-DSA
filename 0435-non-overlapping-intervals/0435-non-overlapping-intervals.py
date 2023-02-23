class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result=0
        
        prevend=intervals[0][1]
        intervals=intervals[1:]
        
        for start,end in intervals:
            if start>=prevend:
                prevend=end
            else:
                
                result+=1
                prevend=min(prevend,end)
       
        return result
            
        
        