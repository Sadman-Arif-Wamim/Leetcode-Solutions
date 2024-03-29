from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = set()
        nums.sort()
        for i in range(0, len(nums)):
            firstNum = nums[i]
            j,k = i+1, len(nums)-1

            while(k > j):
                secondNum = nums[j]
                thirdNum = nums[k]

                sum = firstNum + secondNum + thirdNum
                if(sum > 0):
                    k -= 1
                elif(sum < 0):
                    j += 1
                else:
                    triplet.add((firstNum, secondNum, thirdNum))
                    j += 1
                    k -= 1
        return triplet
                    


            

                        
       
                