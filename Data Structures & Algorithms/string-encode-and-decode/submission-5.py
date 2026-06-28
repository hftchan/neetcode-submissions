class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "Empty"    
        else:
            new_string = "{005}".join(strs)
            return new_string
            
            

    def decode(self, s: str) -> List[str]:
        if s == "Empty":
            return []
        else:
            new_string = s.split("{005}")
            print(new_string)  
            return new_string
