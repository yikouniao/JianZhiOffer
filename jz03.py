
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

class Solution:
    # def findRepeatNumber(self, nums: List[int]) -> int:
    #     d = {}
    #     for num in nums:
    #         if num not in d:
    #             d[num] = 1
    #         else:
    #             return num
    #     return -1    
    
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] != nums[nums[i]]:
                    t = nums[i]
                    nums[i] = nums[t]
                    nums[t] = t
                else:
                    return nums[i]
        return -1
