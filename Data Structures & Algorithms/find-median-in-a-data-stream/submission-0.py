class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        n = len(self.nums)

        # if self.nums is empty 
        if not self.nums:
            self.nums.append(num)
            return 

        # if not empty add in order O(n)
        biggest_flag = False
        for i in range(n):
            if num <= self.nums[i]:
                break
            # if at end and not break, means larger than all elements
            if i == n - 1:
                biggest_flag = True

        if biggest_flag:
            self.nums.append(num)
        else:
            self.nums.insert(i, num)
    
    def findMedian(self) -> float:
        n = len(self.nums)
        m = n // 2
        # if odd take middle 
        if n % 2 == 1:
            return float(self.nums[m])
        # if even take average fo two middle 
        left_middle_index = m - 1
        right_middle_index = m
        return (self.nums[left_middle_index] + self.nums[right_middle_index]) / 2
        
        