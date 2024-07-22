# https://leetcode.cn/problems/product-of-array-except-self/?envType=problem-list-v2&envId=2cktkvj&
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_to_right_multiply = [1]
        right_to_left_multiply = [1]

        for num in nums:
            left_to_right_multiply.append(left_to_right_multiply[-1] * num)
        for num in reversed(nums):
            right_to_left_multiply.append(right_to_left_multiply[-1] * num)
        output = []
        for i in range(len(nums)):
            output.append(left_to_right_multiply[i] * right_to_left_multiply[-2 - i])
        return output
