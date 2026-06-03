class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1>l2:
            return False
        count_1 = [0] * 26
        count_2 = [0] * 26
        for i in range(l1):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1
        
        if count_1 == count_2:
            return True
        
        for i in range(l1, l2):
            count_2[ord(s2[i]) - ord('a')] += 1
            count_2[ord(s2[i-l1]) - ord('a')] -= 1
            if count_1 == count_2:
                return True
        
        return False

        # TC = O(n) , SC = O(1)