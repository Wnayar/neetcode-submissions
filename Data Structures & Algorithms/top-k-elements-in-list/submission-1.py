class Solution:
    # time complexity O(n) due to sort, space O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is number, count is value
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        # make an array where index is frequency and value is list of nums satifying that frew
        freq = [[] for i in range(len(nums) + 1)]
        for key, v in d.items():
            freq[v].append(key)

        # check frequency array for the back 
        res = []
        for i in range(len(freq) - 1, 0, -1 ):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        



        




        