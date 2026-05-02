class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0
        while i<len(chars):
            groups = 1

            while (i+groups)<len(chars) and chars[i] == chars[i + groups]:
                groups += 1
            chars[insert] = chars[i]
            insert += 1
            if groups>1:
                string = str(groups)
                chars[insert: insert+len(string)] = list(string)
                insert += len(string)
            i += groups
        
        return insert
      
                


        