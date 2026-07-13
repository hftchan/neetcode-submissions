class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s
        s = ("".join(filter(str.isalnum,s2))).lower()
        left_hand=0
        right_hand=len(s)-1
        while left_hand<right_hand:
            if s[left_hand] == s[right_hand]:
                left_hand+=1
                right_hand-=1
                continue
            else:
                return False
        return True