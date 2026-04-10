class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len=1
        prev=""
        l=0
        r=1
        window={}
        while r < len(arr):
            if arr[r-1]>arr[r] and prev!=">":
                max_len=max(max_len,r-l+1)
                r+=1
                prev=">"
            elif arr[r-1]<arr[r] and prev!="<":
                max_len=max(max_len,r-l+1)
                r+=1
                prev="<"
            else:
                if arr[r]==arr[r-1]:
                    r=r+1
                else:
                    r
                l=r-1
                prev=""
        return max_len


