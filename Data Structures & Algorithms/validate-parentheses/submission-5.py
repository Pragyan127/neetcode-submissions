class Solution:
    def isValid(self, s: str) -> bool:
        bracs = {')':'(', ']':'[','}':'{'}
        lists = []

        for c in s:
            if c in bracs:
                if lists and lists[-1] == bracs[c]:
                    lists.pop()
                else:
                    return False
            else:
                lists.append(c)
        return len(lists) == 0
            
            

