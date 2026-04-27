class Solution:

    def encode(self, strs: List[str]) -> str:
        lists = []
        for i in strs:
            l = str(len(i))
            lists.append(l+'#'+i)
        return "".join(lists)

    def decode(self, s: str) -> List[str]:
        lists = []
        i = 0 
        while i<len(s):

            j = i
            while s[j] != '#':
                j += 1
            lth = int(s[i:j])
            word = s[j+1:lth+j+1]
            i = lth+j+1
            lists.append(word)
        return lists


       
        



