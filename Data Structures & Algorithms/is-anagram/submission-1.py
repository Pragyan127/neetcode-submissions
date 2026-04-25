class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1 = "".join(sorted(s))
        # s2 = "".join(sorted(t))
        # if s1 == s2:
        #     return True
        # return False

        # return Counter(s) == Counter(t) 

        if len(s) != len(t):
            return False
        
        count = [0]*26
        for i in range(len(s)):
            count [ord(s[i])-ord('a')] +=1
            count [ord(t[i])-ord('a')] -=1

        for i in count:
            if i !=0:
                return False
        return True
           

