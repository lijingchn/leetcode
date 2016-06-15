#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def reverseString(self,s):
        # solution 1
        result = s[::-1]

        # solution 2
#        l = list(s)
#        l.reverse()
#        result = ''.join(l)
        return result

a = Solution()
print a.reverseString("hello")


