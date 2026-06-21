class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # time complexity O(nlogn), space O(1)
        # sort the array 
        nums.sort(reverse=True)

        # go through array return k number
        res = -1001
        for i in range(0, k):
            res = nums[i]

        # get 2nd largest numner
        return res
        