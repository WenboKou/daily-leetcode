# https://leetcode.cn/problems/palindromic-substrings/description/?envType=problem-list-v2&envId=2cktkvj&
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(0, 2 * n - 1):
            l = i / 2
            r = i / 2 + i % 2
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
                ans += 1
        return ans
