# https://leetcode.cn/problems/daily-temperatures/?envType=problem-list-v2&envId=2cktkvj&
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        out_dict = {index:0 for index in range(len(temperatures))}
        stack = [] # (index, temp)
        for index, temp in enumerate(temperatures):
            while stack:
                if stack[-1][1] < temp:
                    out_dict[stack[-1][0]] = index - stack[-1][0]
                    stack.pop(-1)
                else:
                    break
            stack.append((index, temp))
        return out_dict.values()
