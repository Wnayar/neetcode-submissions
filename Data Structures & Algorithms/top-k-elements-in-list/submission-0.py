class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is number, count is value
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        temp = list(set(nums))
        freq = []
        for i in temp:
            freq.append(d[i])
        
        freq.sort(reverse=True)
        top_k_freq = []
        for i in range(k):
            top_k_freq.append(freq[i])
        
        res = []
        for k in d:
            if d[k] in top_k_freq:
                res.append(k)
        
        return res



        




        