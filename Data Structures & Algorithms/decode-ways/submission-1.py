class Solution:
    def numDecodings(self, s: str) -> int:
      #Bottom UP Approach
        # dp = { len(s) : 1}
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i+1]
            
        #     if i+1 < len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in "0123456"):
        #         dp[i] += dp[i+2]
            
        # return dp[0]
       
        if not s or s[0] == '0':
            return 0
        
        prev1, prev2 = 1,1
        for i in range(len(s)-1, -1, -1):
            cur = 0
            if s[i] != '0':
                cur = prev1
            
            if i+1<len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in "0123456") :
                cur += prev2
            prev1, prev2 = cur, prev1

        return prev1
