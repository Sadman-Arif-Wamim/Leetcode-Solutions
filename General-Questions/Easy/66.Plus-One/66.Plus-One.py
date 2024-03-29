from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 1 
        sum = 0
        for i in digits[::-1]:
            print(i)
            sum += i * count
            count = count * 10
        sum += 1
        return [int(x) for x in str(sum)]
        