class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort(key = lambda x : x[0])
        prev=intervals[0]
        
        for i in range(1,len(intervals)):
            
            if prev[1]<intervals[i][0]:
                result.append(prev)
                prev=intervals[i]
                
            prev=[min(prev[0],intervals[i][0]),max(prev[1],intervals[i][1])]
        
        result.append(prev)
        return result
        
        
        
        