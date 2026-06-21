class Solution:

    # "test", "me"  --encode--> 4#test2#me  --decode--> "test", "me"
    def encode(self, strs: List[str]) -> str:
        res = ""
        d = "#"

        for w in strs:
            l = len(w)
            temp = str(l) + d + w
            res += temp

        return res 


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        temp = ""
        length = len(s)
        
        while i < length:
            if s[i] == "#":
                size = int(temp)
                w = s[i + 1: i + size + 1]
                res.append(w)
                i = i + size + 1
                temp = ""
                continue 
            
            
            temp += s[i]
            i += 1

        return res 




