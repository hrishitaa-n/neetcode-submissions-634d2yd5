class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_list=set(nums)
        longest=0
        length=0
        for num in nums_list:
            if num-1 not in nums_list:
                current=num
                length=1
                while current+1 in nums_list:
                    length+=1
                    current=current+1

            longest = max(longest, length)
        return longest