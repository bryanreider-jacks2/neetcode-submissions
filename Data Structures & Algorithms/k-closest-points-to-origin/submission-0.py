class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pts = {}
        res = []

        for i, point in enumerate(points):
            x, y = point[0], point[1]
            distance = (math.sqrt(x**2 + y**2))

            pts[(distance, i)] = point

        distances = list(pts.keys())
        heapq.heapify(distances)

        for i in range(k):
            smallest = heapq.heappop(distances)
            res.append(pts[smallest])

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