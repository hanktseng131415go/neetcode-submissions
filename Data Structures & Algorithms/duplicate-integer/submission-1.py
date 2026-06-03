class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map = set()
        for n in nums:
            if n not in h_map:
                h_map.add(n)
            else:
                return True

        return False