class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = []
        n = len(temp)
        ans = [0] * n

        for i, t in enumerate(temp):
            while stk and stk[-1][0] < t:
                tmp, idx = stk.pop()
                ans[idx] = i-idx
            stk.append([t, i])
        
        return ans
# TC, SC = O(n)