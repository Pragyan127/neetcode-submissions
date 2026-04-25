class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seq = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seq:
                seq.remove(s[l])
                l += 1
            seq.add(s[r])
            
            result = max(result, r-l+1)
        return result