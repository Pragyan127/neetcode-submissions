class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[-1]:
                l = 0
                r = n-1
                while l <= r:
                    mid = (r+l) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        l = mid+1
        return False
        # TC = O(m logn), SC = O(1)

