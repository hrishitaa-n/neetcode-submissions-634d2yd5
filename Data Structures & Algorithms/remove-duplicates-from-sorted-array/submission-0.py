class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        fast=1
        while fast<len(nums):
            if nums[slow]==nums[fast]:
                fast+=1
            elif nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            
        return slow+1   
          
            

        