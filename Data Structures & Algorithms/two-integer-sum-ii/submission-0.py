class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1
        i = 0
        j = n
        while i<j:
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1