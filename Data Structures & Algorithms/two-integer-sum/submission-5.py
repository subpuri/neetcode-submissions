class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0]*2
        hash = dict()
        k = 0
        for x in nums:
            if target-x in hash:
                ans[0] = hash[target-x]
                ans[1] = k
                return ans
            else:
                hash[x] = k
                k = k+1
 


        