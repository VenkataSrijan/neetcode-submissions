class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        seen = set()
        count = 0

        while j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i+=1
            count = max(count,j-i)

        return count