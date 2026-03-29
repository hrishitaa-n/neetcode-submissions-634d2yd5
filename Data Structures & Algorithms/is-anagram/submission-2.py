class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        count2={}
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
        for j in range(len(t)):
            count2[t[j]]=count2.get(t[j],0)+1
        if count==count2:
            return True
        return False

        