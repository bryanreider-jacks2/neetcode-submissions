class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            l += 1
        return nums[l]


        

'''
[1,2,3,4,5,6]

[3,4,5,6,1,2]

         l
           r

'''