class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # How does anyone think of this solution omg -_-

        left, right = [], []

        leftPrefix = 1
        rightPrefix = 1

        product = []
        for i in range(len(nums)):
            left.append(leftPrefix)
            leftPrefix *= nums[i]

        for j in range(len(nums)-1, -1, -1):   
            right.append(rightPrefix)
            rightPrefix *= nums[j]
        
        for i in range(len(nums)):
            product.append(left[i]*right[len(nums)-1-i])
        return product