class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        def binary_search(left: int, right: int):
            while left <= right:
                middle = (left + right) // 2
                if target == nums[middle]:
                    return middle
                elif target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1

        res = binary_search(0, pivot - 1)

        if res != -1:
            return res
        
        return binary_search(pivot, len(nums) - 1)
        


'''
[6,1,2,3,4,5] target = 4
  


'''