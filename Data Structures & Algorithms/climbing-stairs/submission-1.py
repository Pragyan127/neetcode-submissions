# Bottom Up Tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n==2:
            return 2
        db = [0] *n
        db[0] = 1
        db[1] = 2
        for i in range(2,n):
            db[i] = db[i-1]+db[i-2] 
    
        
        return db[n-1]
#Time : O(n)
#space : O(n)

        