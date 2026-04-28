class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        truth = [False] * (len(s) + 1)
        truth[0] = True

        for i in range(len(s)):
            if truth[i]:
                for j in range(i+1,len(s)+1 ):
                    if s[i:j] in wordset:
                        truth[j] = True
        return truth[len(s)]