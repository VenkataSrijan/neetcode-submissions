import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        for num in nums:
            dict[num] +=1
        
        items = heapq.nlargest(k,dict.values())
        res = []
        
        for key, val in dict.items():
            if val in items:
                res.append(key)
        
        return res
