class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = len(numbers)-1
        right = 0
        sum= numbers[left] + numbers[right]
        while sum != target:
            if sum>target:
                left-=1
            if sum<target:
                right+=1 
            sum = numbers[right] + numbers[left]
        return [right+1,left+1]