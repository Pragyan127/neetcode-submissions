class Solution:
    def ispalin(self, s,l,r):
        local_count = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            local_count += 1
            l -= 1
            r += 1
        return local_count

    def countSubstrings(self, s: str) -> int:
        total_count = 0
        for i in range(len(s)):
            total_count += self.ispalin(s, i, i)
            total_count += self.ispalin(s, i, i+1)
        return total_count
    
        return self.countSubstrings(s)

# TC = O(n^2)
#SC = O(1)