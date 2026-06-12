class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            if i == 0:
                output[i] = 1
            else:
                prefix = prefix*nums[i-1]
                output[i] = prefix

        for i in range(len(nums)-2,-1,-1):
            postfix = postfix*nums[i+1]
            output[i] = postfix*output[i]

        return output
            