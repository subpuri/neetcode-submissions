class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0]*2
        hash = dict()
        k = 0
        for x in nums:
            hash[x] = k
            k = k+1

        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                ans[0] = i
                ans[1] = hash[target-nums[i]]
                return ans
        return ans 

        