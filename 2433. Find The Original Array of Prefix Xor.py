class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pr = [pref[0]]
        y=0
        for i in range(1,len(pref)):
            y = y^pr[i-1]
            x = y^pref[i]
            pr.append(x)
        return pr
