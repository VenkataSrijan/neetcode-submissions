class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        dict = defaultdict(int)
        maxLength = 0

        while j<len(s):
            dict[s[j]]+=1
            while (j-i+1 - max(dict.values()))>k:
                dict[s[i]]-=1
                i+=1
            maxLength = max(maxLength,j-i+1)
            j+=1

        return maxLength