class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        for j in range(len(nums)):
            if nums[j] in window:
                return True
            
            window.add(nums[j])
            
            if len(window) > k:
                window.remove(nums[j - k])
        
        return False