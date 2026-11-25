class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        stack = []
        out = []
        for x, y in points:
            stack.append(((x**2 + y**2)**0.5, (x, y)))

        heapq.heapify(stack)
        while k > 0:
            out.append(heapq.heappop(stack)[1])
            k-=1

        return out