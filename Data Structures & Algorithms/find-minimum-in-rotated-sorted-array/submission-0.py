class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 100000

        while r>=l:
            m = (r+l)//2 #find mid point
            if nums[r]>nums[l]:
                #this means its sorted 
                res = min(res,nums[l])
                break
                #nums has to be the smallest value within sorted

            if nums[m] > nums[r]:
                l = m + 1
                res = min(res,nums[m])
            else:
                r = m - 1
                res = min(res,nums[m])
        return res