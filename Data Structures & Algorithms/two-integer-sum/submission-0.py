class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            substract = target - num
            if substract in seen:
                return [seen[substract], i]
            seen[num] = i
        return None