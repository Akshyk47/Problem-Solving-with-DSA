#User function Template for python3

class Solution:
    def PartyType(self, a, n):
        
        robes=set()
        
        for num in a:
            if num in robes:
                return 'BOYS'
            else:
                robes.add(num)
        return 'GIRLS'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.PartyType(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends