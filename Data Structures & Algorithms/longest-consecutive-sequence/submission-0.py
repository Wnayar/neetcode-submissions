class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        
        # check for longest sequence, achieved by checking no before, and check after
        for i in s:
            # not start of partitioned sequence 
            if i - 1 in s:
                continue 
            # start of sequence 
            length = 0
            while i + length in s:
                length += 1

            # get max longest 
            longest = max(length, longest)
            
        return longest