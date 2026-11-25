class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # time: nlogn
        # space; k
        self.stack, self.k = nums, k
        heapq.heapify(self.stack)
        while len(self.stack) > k:
            heapq.heappop(self.stack)

    def add(self, val: int) -> int:
        heapq.heappush(self.stack, val)
        if len(self.stack) > self.k:
            heapq.heappop(self.stack)
        
        return self.stack[0]
