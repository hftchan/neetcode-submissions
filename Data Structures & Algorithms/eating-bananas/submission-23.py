import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        best = right
        while left<=right :
            mid = left + (right-left)//2
            total_time = 0

            for i in piles:
                total_time += math.ceil(i/mid)
            
            if total_time<=h and best>mid:
                best = mid
                right = mid-1
            else:
                left = mid+1

        return best