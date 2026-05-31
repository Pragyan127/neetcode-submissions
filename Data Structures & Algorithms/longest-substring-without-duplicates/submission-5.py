class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seq = set()
        res = 0

        for i in range(len(s)):
            while s[i] in seq:
                seq.remove(s[l])
                l += 1
            seq.add(s[i])
            res = max(res, i-l+1)
        return res
# TC, SC = O(n)