class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for ch in s:
            if (ch.isalnum()):
                text += ch
        
        string = text.lower()
        i,j = 0,len(string)-1

        while i<j:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        
        return True