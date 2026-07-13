class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest_num=0
        st = set()

        for i in nums:
            st.add(i)
        
        for i in nums:
            if i in st and i-1 not in st:
                cur = i
                cnt = 0

                while cur in st:
                    cur+=1
                    cnt+=1
                largest_num = max(cnt, largest_num)

        return largest_num