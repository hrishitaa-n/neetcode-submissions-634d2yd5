class Solution:
    def twoSum(self, nums, target):
       hashs={}
       
       for i in range(len(nums)):
        j=target-nums[i]
        if j in hashs:
            return [hashs[j],i]
        else:
            hashs[nums[i]] = i
        
        