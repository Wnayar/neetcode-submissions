class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lhs = 0
        rhs = len(nums) - 1 

        # 1 number
        if len(nums) == 1: 
            print("here")
            if nums[0] == target:
                return 0
            else:
                return -1        
        # 2 numbers
        elif len(nums) == 2: 
            if nums[lhs] == target:
                return lhs
            elif nums[rhs] == target:
                return rhs 
            else:
                return -1
        #rest
        else:
            while lhs <= rhs:
                mid = math.ceil((lhs + rhs) / 2)
                if nums[mid] == target:
                    return mid
                elif rhs - lhs == 0:
                    if nums[lhs] == target:
                        return lhs
                    lhs = lhs + 1                    
                elif rhs - lhs == 1:
                    if nums[lhs] == target:
                        return lhs
                    elif nums[rhs] == target:
                        return rhs
                    else:
                        lhs = lhs + 1
                elif nums[mid] < target:
                    lhs = mid + 1
                elif nums[mid] > target:
                    rhs = mid - 1

            return -1