class Solution:
    def twoSum(self, nums, target):
        hash={}
        for i in range(len(nums)):
            second_num=target-nums[i]
            if second_num in hash:
                return [hash[second_num], i]
            hash[nums[i]]=i