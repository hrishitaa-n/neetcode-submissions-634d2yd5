class Solution:
    def twoSum(self, nums, target):
        hash={}
        for i in range(len(nums)):
            current=nums[i]
            complement=target-current
            if complement in hash:
                return [hash[complement],i]
            hash[current]=i