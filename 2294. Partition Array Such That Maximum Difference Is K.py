class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        st = nums[0]
        for i in range(len(nums)):
            d = nums[i] - st
            if d >k:
                ans+=1
                st = nums[i]
        return ans
