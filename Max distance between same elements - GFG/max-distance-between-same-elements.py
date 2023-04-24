class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        max_dist=0
        ele_ind_map={}
        
        for i in range(len(arr)):
            if arr[i] in ele_ind_map:
                max_dist=max(max_dist,i-ele_ind_map[arr[i]])
            else:
                ele_ind_map[arr[i]]=i
        
        return max_dist



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends