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
        num = -1
        # temp is used to store temporary number and strings 
        temp = ""
        res = []
        d = "#"

        for c in s:
            if c == d and num < 0:
                num = int(temp)
                if num == 0:
                    res.append("")
                temp = ""
                continue 

            temp += c
            num -= 1

            if num == 0:
                res.append(temp)
                temp = ""


        return res 


