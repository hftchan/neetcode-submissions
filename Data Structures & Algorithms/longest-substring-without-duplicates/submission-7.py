class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #tracker = defaultdict(set)
        right=1
        left=0
        max_len = 0
        new_length = 0 
        if len(s) == 1:
            return 1
        while right<len(s):

            current_arr = s[left:right]
            #Check new length each time, but only calculate when unique  

            new_length = len(current_arr)
            max_len = max(new_length, max_len)
            
            if s[right] in current_arr :
                    left+=1
            else:
                    right+=1
                    current_arr = s[left:right]
                    new_length = len(current_arr)
                    max_len = max(max_len, new_length)
            

            #Find a way to check it if a duplicate is added 
            #Or see if the intended to be added element is a duplicate
            #if so we need to increase the left pointer to keep moving forward
            #The reason why it doesn't matter is mainly because the substring was
            #bounded by the two repeating characters anyways, so there was a limit to how long it could be 

        return max_len 



