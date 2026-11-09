class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            weight_diff = x - y
            if weight_diff > 0:
                heapq.heappush_max(stones, weight_diff)

        stones.append(0)
        return stones[0]





"""
stones = [2,2,3,4,6]
x = 2
y = 2
total = 0

"""
        