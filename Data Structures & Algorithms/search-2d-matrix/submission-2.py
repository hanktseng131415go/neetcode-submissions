class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_l, r_r = 0, len(matrix) - 1
        while r_l <= r_r:
            r_m = r_l + (r_r - r_l) // 2
            if target < matrix[r_m][0]:
                r_r = r_m - 1
            elif matrix[r_m][-1] < target:
                r_l = r_m + 1

            else:
                break
        
        # if not r_l <= r_r:
        #     return False

        l_l, l_r = 0, len(matrix[r_m]) - 1
        while l_l <= l_r:
            l_m = l_l + (l_r - l_l) // 2
            if target < matrix[r_m][l_m]:
                l_r = l_m - 1
            elif target > matrix[r_m][l_m]:
                l_l = l_m + 1
            else:
                return True

        return False
