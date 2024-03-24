class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height) - 1

        while(j > i):
            hI = height[i]
            hJ = height[j]

            if(hI > hJ):
                area = hJ * (j-i)
                j -= 1
            else:
                area = hI * (j-i)
                i += 1
            
            if(area > maxArea):
                maxArea = area
        return maxArea