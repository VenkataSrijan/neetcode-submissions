class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        i=0
        j = len(height)-1
        leftMax = height[i]
        rightMax = height[j]
        
        while i<j:
            if leftMax < rightMax :
                if leftMax-height[i]>0:
                    count += leftMax - height[i]
                i+=1
                leftMax = max(leftMax,height[i])

            else:
                if rightMax-height[j]>0:
                    count+= rightMax - height[j]
                j-=1
                rightMax = max(rightMax,height[j])
        
        return count

