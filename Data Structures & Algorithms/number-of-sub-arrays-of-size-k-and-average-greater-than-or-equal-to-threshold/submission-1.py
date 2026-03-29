class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        count = 0
        
        for j in range(len(arr)):
            window_sum += arr[j]
            
            if j >= k:
                window_sum -= arr[j - k]
            
            if j >= k - 1 and window_sum/k >=threshold:
                count += 1
        
        return count