class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        frequency1={}
        frequency2={}
        for ch in range(len(s1)):
            frequency1[s1[ch]]=1+frequency1.get(s1[ch],0)
        for right in range(len(s2)):
            frequency2[s2[right]]=1+frequency2.get(s2[right],0)
            while right - left + 1>len(s1):
                frequency2[s2[left]]-=1
                if frequency2[s2[left]]==0:
                    del frequency2[s2[left]]
                left+=1
            if frequency1==frequency2:
                 return True
        return False