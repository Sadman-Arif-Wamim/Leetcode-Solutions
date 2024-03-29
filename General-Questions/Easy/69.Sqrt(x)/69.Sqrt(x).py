class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while(right >= left):
            middle = (right - left)//2 + left
            if middle > x//middle:
                right = middle - 1
            elif middle < x//middle:
                left = middle + 1
            else:
                return middle
        return right