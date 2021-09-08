# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        n = len(nums)
        limit = n / 2
        for num in nums:
            m[num] = m.get(num, 0) + 1
            if m[num] >= limit:
                return num
        return nums[0]
