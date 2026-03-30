class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        window_sum=0
        min_array = float('inf')
        for right in range(len(nums)):
            window_sum+=nums[right]
            while window_sum>=target:
                min_array=min(min_array,right-left+1)
                window_sum-=nums[left]
                left+=1
        return 0 if min_array == float('inf') else min_array


        