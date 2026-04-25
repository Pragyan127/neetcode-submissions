class Solution:

    def encode(self, strs: List[str]) -> str:
        combo=[]
        for i in strs:
            l = len(i)
            aa=((str(l))+"$"+i)
            combo.append(aa)
        enc = "".join(combo)
        return enc


    def decode(self, s: str) -> List[str]:
        final = []
        i=0

        while i<len(s):

            j=i
            while s[j] != "$" :
                j += 1
            lth = int(s[i:j])
            word = s[j+1:j+1+lth]
            final.append(word)
            i = j + 1 + lth

        return final



