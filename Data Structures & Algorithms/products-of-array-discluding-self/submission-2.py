class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        res = []

        mul = 1

        for num in nums:
            left.append(mul)
            mul *= num
        
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(mul)
            mul *= nums[i]

        for j in range (0, len(nums)):
            res.append(left[j]*right[len(nums)-1-j])

        return res