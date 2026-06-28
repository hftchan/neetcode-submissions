class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        for i in nums:
            res[i]+=1
        sorted_dict=(sorted(res.items(), key=lambda item:item[1]))
        ans=[]
        for i in range(1,k+1):
            ans.append(sorted_dict[-i][0])       
        return ans

