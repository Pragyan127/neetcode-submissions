class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        MAX = 0x7fffffff
        
        while (mask&b)>0:
            a, b = a^b , (a&b) << 1
        return (mask&a) if b>0 else a
        # TC(At most 32 iterations), SC = O(1), 