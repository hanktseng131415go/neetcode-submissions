class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # one pass
        # time: logmn
        # space: 1
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row*col - 1
        while l <= r:
            m = l + (r - l) // 2
            v = matrix[m//col][m%col]
            if v < target:
                l = m + 1
            elif target < v:
                r = m - 1
            else:
                return True
        
        return False

        # # two pass
        # # time: logmn
        # # space: 1
        # r_l, r_r = 0, len(matrix) - 1
        # while r_l <= r_r:
        #     r_m = r_l + (r_r - r_l) // 2
        #     if target < matrix[r_m][0]:
        #         r_r = r_m - 1
        #     elif matrix[r_m][-1] < target:
        #         r_l = r_m + 1

        #     else:
        #         break

        # l_l, l_r = 0, len(matrix[r_m]) - 1
        # while l_l <= l_r:
        #     l_m = l_l + (l_r - l_l) // 2
        #     if target < matrix[r_m][l_m]:
        #         l_r = l_m - 1
        #     elif target > matrix[r_m][l_m]:
        #         l_l = l_m + 1
        #     else:
        #         return True

        # return False
