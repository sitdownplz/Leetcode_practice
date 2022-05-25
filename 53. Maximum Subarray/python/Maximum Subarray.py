## Leetcode Practice
# -- 53. Maximum Subarray --

# Solution
# Runtime: 776 ms, Memory: 28 MB
class Solution:
    def maxSubArray(nums) -> int:
        assert(isinstance(nums,list))
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i]+nums[i-1])
        return max(nums)

# Main
testcase_1 = [-2,1,-3,4,-1,2,1,-5,4]
testcase_2 = [1]
testcase_3 = [5,4,-1,7,8]

sol = Solution.maxSubArray(testcase_1)
print(sol)