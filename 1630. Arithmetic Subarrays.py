class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
                
        def check(k,n,d):
            for i in range(n-1):
                if k[i+1]-k[i] != d:
                    print(k[i+1],k[i],"d=",d)
                    return False
            return True
        
        if len(set(nums))==1:
            return len(nums)*[True]
        ans = []
        for i,j in zip(l,r):
            k=nums[i:j+1]
            k.sort()
            if(check(k,len(k),k[1]-k[0])):
                ans.append(True)
            else:
                ans.append(False)
        return ans
