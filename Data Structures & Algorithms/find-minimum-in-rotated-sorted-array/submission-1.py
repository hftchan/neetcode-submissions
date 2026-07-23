class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = 100000
        while left <= right:
            mid = (left + right)//2
            #In every situation it keeps on storing smallest that it encounters
            if nums[left] < nums[right]:
                #this is definitely sorted
                res = min(res, nums[left])

            if nums[mid]<nums[right]:
                right = mid - 1
                res = min(res,nums[mid])
            else:
                left = mid + 1
                res = min(res, nums[mid])
        return res