class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge case duplicate number
        if target % 2 == 0:
            # check for duplicate number
            half_target = target / 2
            temp_list = []
            for x, number in enumerate(nums):  
                if number == half_target:
                    temp_list.append(x)
            if len(temp_list) == 2:
                return temp_list

        # make a dict key is numerical value, and value is index 
        num_dict = {}
        for i, number in enumerate(nums):
            num_dict[number] = i
        print(num_dict)
        for j in num_dict:
            k = num_dict.get(target - j)
            if k and k != num_dict.get(j):
                return [num_dict.get(j), k]
