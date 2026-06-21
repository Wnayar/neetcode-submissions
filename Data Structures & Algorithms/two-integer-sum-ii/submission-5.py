class Solution:
    # essentially removing candinates i.e if sum too big u already have smallest on left so need to reduce right 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                return [l + 1, r + 1]
         