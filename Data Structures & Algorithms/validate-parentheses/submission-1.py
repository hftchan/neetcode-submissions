class Solution:
    def isValid(self, s: str) -> bool:
        idx = -1
        arr =[0]*len(s)
        for c in s:
            if c == "{" or c == "[" or c == "(":
                idx+=1
                arr[idx] = c
            else:
                if c== "}"  and arr[idx] =="{":
                    idx-=1
                elif c == ")" and arr[idx] == "(":
                    idx-=1
                elif c == "]" and arr[idx] == "[":
                    idx-=1
                else:
                    return False
        if idx!=-1:
            return False
        return True

        
