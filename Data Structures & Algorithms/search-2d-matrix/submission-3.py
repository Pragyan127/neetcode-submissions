class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rw = len(matrix)
        cl = len(matrix[0])
        l = 0
        r = rw * cl - 1

        while l <= r:
            mid = (l+r) // 2
            row = mid // cl
            col = mid % cl

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
#TC = O(log(m*n)) , SC = O(1)

