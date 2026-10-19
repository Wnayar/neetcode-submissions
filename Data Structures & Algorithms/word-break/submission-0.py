class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create memo dict 
        dic = {}
        # use a pointer vairable to track or operations 
        res = [False]

        # define recursion function 
        def recur(i):
            # check cache 
            if i in dic:
                return 
                
            # base case if reach end of s, set res[0] to be true 
            if i == len(s):
                res[0] = True
                return  
             
            # recursion 
            for w in wordDict:
                if s.startswith(w, i):
                    recur(i + len(w))
            
            # add to cache 
            dic[i] = False 
            
            # base case 2, where cant go any further and not at end 
            return 
        
        # call dp and return result
        recur(0)
        return res[0]