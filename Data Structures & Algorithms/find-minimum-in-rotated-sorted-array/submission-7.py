class Solution:
    def findMin(self, nums: List[int]) -> int:
        # there is a bigger portion and smaller portion
        # [5, 6, 7, 8, 9, 10, 3, 4, 5]
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if already sorted return 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = l + ((r - l) // 2)
            res = min(res, nums[m])
            # need to be mroe than equal for case of 2 elemnts left division will make m = 0, and l is 0 so will comapre both, thus need mroe than equal to force l to m + 1 so that we dont miss out right element, if ditn goes to other branch and we skip an element
            if nums[m] >= nums[l]:
                # if at least one rotation, in bigger portion
                l = m + 1
            else:
                # im in smaller portion so i want to go left
                r = m - 1

        return res 
        