class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()

        def dfs(i, soln, total):
            if target == total:
                res.append(soln.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                soln.append(nums[j])
                dfs(j, soln, total + nums[j] )
                soln.pop()
        dfs(0, [], 0)

        return res



        