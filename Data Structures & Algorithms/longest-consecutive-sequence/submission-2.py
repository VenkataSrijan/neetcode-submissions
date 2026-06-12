class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        maxCount = 0

        for num in res:
            count = 0
            if num-1 not in res:
                while num in res:
                    count+=1
                    num = num+1
            maxCount = max(maxCount,count)

        return maxCount
