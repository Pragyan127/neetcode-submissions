class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        lengths= set(len(w) for w in wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True
        n = len(s)

        for i in range(n):
            if not dp[i]:
                continue
            for l in lengths:
                j = i+l
                if j <= n and s[i:j] in wordDict:
                    dp[j] = True
        return dp[n] #TC = O(n · k · t), SC = O(m · t)