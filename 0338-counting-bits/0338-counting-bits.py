class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        result=[]
        for number in range(n+1):
            countof1=self.count_1bit(number)
            result.append(countof1)
        
        return result
    
    def count_1bit(self,num: int) -> int:
            count=0
            while num:
                count+=num & 1
                num=num>>1
            return count
        