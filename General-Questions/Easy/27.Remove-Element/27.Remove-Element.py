class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_copy = nums[:]
        for i in range(len(nums_copy)):
          if nums_copy[i] == val:
            nums.remove(nums_copy[i])
        return len(nums)
        
        