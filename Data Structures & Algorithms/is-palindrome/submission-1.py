class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(c):
            if (ord('a')<=ord(c)<=ord('z')):
                return True
            elif(ord('0')<=ord(c)<=ord('9')):
                return True
            elif (ord('A')<=ord(c)<=ord('Z')):
                return True
            else:
                return False
        r = len(s)-1
        l = 0
        while l<r:
            while l<r and not isalphanum(s[r]):
                r -= 1
            while l<r and not isalphanum(s[l]):
                l += 1
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1
        return True

        