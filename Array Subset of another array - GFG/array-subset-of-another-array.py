#User function Template for python3

def isSubset( a1, a2, n, m):
    
    arr1_map={}
    for num in a1:
        arr1_map[num]=arr1_map.get(num,0)+1
    
    for number in a2:
        if (number in arr1_map) and (arr1_map[number]>0):
            arr1_map[number]-=1
        else:
            return 'No'
    return 'Yes'
        
            
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends