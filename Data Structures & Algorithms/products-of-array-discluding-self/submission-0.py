class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_arr=[0]*length
        postfix_arr=[0]*length
        prefix_arr[0] = nums[0]
        postfix_arr[-1] = nums[-1]
        ans = []

        for i in range(1,len(nums)):
            prefix_arr[i] = prefix_arr[i-1]*nums[i]
            postfix_arr[length-1-i]=postfix_arr[length-i]*nums[length-i-1]

        ans.append(postfix_arr[1])
        
        for i in range(1,length-1):
            ans.append(prefix_arr[i-1]*postfix_arr[i+1])
        ans.append(prefix_arr[length-2])
        print(ans)
        return ans
            
        