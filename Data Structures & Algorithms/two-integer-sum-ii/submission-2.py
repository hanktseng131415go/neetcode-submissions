class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, m in enumerate(numbers):
            dif = target - m
            for j, n in enumerate(numbers):
                if j == i:
                    continue
                
                if n == dif:
                    return [i+1, j+1]