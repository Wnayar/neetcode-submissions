class TimeMap:

    def __init__(self):
        self.dict1 = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key: alice, value: (1, happy)
        if self.dict1.get(key) is None:
            self.dict1[key] = []

        self.dict1[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dict1.get(key)

        if lst is None:
            return ""
        
        # binary search 
        l, r = 0, len(lst) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            cur = lst[m][0]

            if cur < timestamp:
                res = lst[m][1]
                l = m + 1
            elif cur > timestamp:
                r = m - 1
            else:
                # equal 
                return lst[m][1] 
        
        return res





        
        


  

        
