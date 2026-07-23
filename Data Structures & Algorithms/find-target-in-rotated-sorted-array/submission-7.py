class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Assume that when you split it
        #one half is always sorted
        left = 0
        right = len(nums) -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            #Sorted half is left

            if nums[left]<=nums[mid]:
                #then decide which half is it in
                if nums[left]<=target<=nums[mid]:
                #if it is within sorted half then move right to middle
                    right = mid 
                else:
                    #if it is not within it
                    left = mid + 1
            #sorted half is the right:
            else:
                if nums[mid]<=target<=nums[right]:
                    #Target is within the half that is sorted
                    left = mid
                else:
                    #target is in unsorted left half:
                    right = mid - 1 #as we consider mid as being part of the sorted part, mid should not be included in the new right
        return -1


        