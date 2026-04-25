class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new_str = ""
        # for char in s:
        #     if char.isalnum():
        #         new_str += char.lower()
        # return new_str == new_str[::-1]

        l , r = 0, len(s)-1
        
        while l<r:
            while l<r and not self.alpha(s[l]):
                l +=1
            while r>l and not self.alpha (s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l , r = l+1, r-1
        return True

    def alpha(self, x):
        return ((ord('a')<=ord(x)<=ord('z')) or
                (ord('A')<=ord(x)<=ord('Z')) or
                (ord('0')<=ord(x)<=ord('9')))


        