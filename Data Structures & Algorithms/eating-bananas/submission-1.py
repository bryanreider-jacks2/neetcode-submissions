class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)              #[1,2,3,4]
        res = r
        while l <= r:
            k = (l + r) // 2            # 
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
 
        return res
                
                    















'''
piles = []          -> no. of bananas
h = 9                -> hours permitted to eat bananas 
k = [1,2,3,4,5,6,7,8,9]                -> eating rate
     l
       r
       m 
O(log(max(piles)) * len(piles))


'''
        