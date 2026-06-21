class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for index, i in enumerate(nums):
            if hashtable.get(i, -1) == -1:
                hashtable[i] = [index]               
            else:
                hashtable[i].append(index)

        for i in hashtable:
            if hashtable.get(target - i, -1) != -1:
                if target - i == i:
                    try:
                        hashtable.get(i)[1]
                    except:
                        continue
                    return [hashtable.get(i)[0], hashtable.get(i)[1]]
                else:
                    return [hashtable.get(i)[0], hashtable.get(target - i)[0]]