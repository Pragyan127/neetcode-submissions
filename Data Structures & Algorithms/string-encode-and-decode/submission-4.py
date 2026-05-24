class Solution:
    def encode(self, strs: List[str]) -> str:
        lists = []
        for wrd in strs:
            n = len(wrd)
            lists.append(str(n) +'' + wrd)
        return ''.join(lists)
    def decode(self, s: str) -> List[str]:
        i = 0
        lists = []

        while i<len(s):
            j = i
            while s[j] != '':
                j += 1
            lth = int(s[i:j])
            word = s[j+1 : j+lth+1]
            lists.append(word)
            i = j+lth+1
        return lists
