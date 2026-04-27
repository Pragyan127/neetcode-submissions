class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):
            #for odd string
            l,r = i,i
            while l >= 0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r += 1
            # for even length string
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r += 1
        
        return res

#TC = For each i → O(n) = Total → n * O(n) = O(n^2)
#SC = O(n)  (due to storing result string) , worst case len of str = res length
