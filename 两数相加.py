# https://leetcode.cn/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def get_number(l):
            return l.val + 10 * get_number(l.next) if l.next else l.val

        l1_number = get_number(l1)
        l2_number = get_number(l2)

        l = l1_number + l2_number

        def build_l(l):
            l_val = l % 10
            l_next = l // 10
            if l_next:
                return ListNode(l_val, build_l(l_next))
            else:
                return ListNode(l_val, None)

        return build_l(l)
