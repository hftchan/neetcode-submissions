class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        sortednums = sorted(nums)
        ans=[]
      
        for i in range(length-1):
            left = i+1
            right = length-1
            sum = sortednums[i] + sortednums[left] + sortednums[right]
            while left<right:
                if sortednums[i]>0:
                    break
                if sum == 0 and [sortednums[i],sortednums[left], sortednums[right]] not in ans:
                    ans.append([sortednums[i], sortednums[left], sortednums[right]])
                    left+=1
                    right-=1
                    third_pos=i
                    sum = sortednums[i] + sortednums[left] + sortednums[right]
                elif sum>0:
                    right-=1
                    sum = sortednums[i] + sortednums[left] + sortednums[right]
                elif sum<0:
                    left+=1
                    sum = sortednums[i] + sortednums[left] + sortednums[right]
                else: 
                    left+=1
                    sum = sortednums[i] + sortednums[left] + sortednums[right]
        return ans


            
             
        