class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        triplets = set()
        nums.sort()

        for i in range(len(nums)-2):
            j = i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k] == -nums[i]:
                    triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
                    if (triplet not in triplets):
                        res.append([nums[i],nums[j],nums[k]])
                        triplets.add(triplet)
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] < -nums[i]:
                    j+=1
                else:
                    k-=1

        return res