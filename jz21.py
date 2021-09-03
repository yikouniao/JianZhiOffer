# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = [num for num in nums if num % 2]
        even = [num for num in nums if not num % 2]
        return odd + even
