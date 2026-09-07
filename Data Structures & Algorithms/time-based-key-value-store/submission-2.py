class TimeMap:

    def __init__(self):
        self.nums = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.nums:
            self.nums[key] = []
        
        self.nums[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.nums:
            return ""
        l, r = 0, len(self.nums[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            
            if self.nums[key][m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return self.nums[key][r][0] if r >= 0 else ""