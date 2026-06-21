class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor, same bit is 0, diff bit is 1
        # communiative (order doesnt matter) and associative (change paranethesis freely)
        # if A xor 0 is A, because 1 ^ 0 is 1 and 0 ^ 0 is 0.
        # xor same A ^ A will be zero 
        res = 0
        for i in nums:
            res = res ^ i
        return res