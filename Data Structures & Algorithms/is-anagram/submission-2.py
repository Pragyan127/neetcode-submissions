class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(t)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for i in count:
            if i != 0:
                return False

        return True
# TC = O(n+26) SC = O(26)
        # Counter[s] == Counter[t]