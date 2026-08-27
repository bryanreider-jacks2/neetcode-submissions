import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        #products to the left
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
        


'''
[1,2,4,6]

[48,24,12,8]
right = 1 * 6 * 4 * 2
output = [48,24,12,8]

[-1,0,1,2,3]
right = 1 * 3 * 2 * 1 * 0
output = [0,-6,0,0,0]


'''


        