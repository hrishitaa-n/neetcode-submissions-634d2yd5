class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        count1={}
        if len(s)!=len(t):
            return False
        for x in range(len(s)):
            count[s[x]]=count.get(s[x],0)+1
        for y in range(len(t)):
            count1[t[y]]=count1.get(t[y],0)+1
        if count==count1:
            return True 
        else:
            return False
            

        