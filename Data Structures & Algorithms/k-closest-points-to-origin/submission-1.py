class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        res = []

        for x,y in points:
            distance = x**2 + y**2
            heap.append((distance,x,y))

        heapq.heapify(heap)

        for i in range(k):
            smallest = heapq.heappop(heap)
            x, y = smallest[1], smallest[2]
            res.append([x,y])

        return res





        
"""

distance = (sqrt(xi^2 + yi^2))
[2, sqrt(8)]
[[0,2],[2,2]]


pts =   {
            (2, 0) : [0,2],
            (sqrt(8), 1): [2,2]
        }
"""