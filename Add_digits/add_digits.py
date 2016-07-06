#!/usr/bin/env python
# encoding: utf-8

# 题目：给定一个非负整数num，重复地将其每位数字相加，直到结果只有一位数为止。
# 例如：给定num = 38, 过程：3 + 8 = 11, 1 + 1 = 2 因为2只有一位，返回2

# 进一步思考：你可以不用循环，在o(1)运行时间内完成题目吗？
# 提示：一个直观的解法就是模拟上述过程，你可以想到别的方法吗？
#       结果一共有多少种可能性？
#       它们是周期性出现的还是随机出现的？

# ****************************************************************************
# 方法一：(使用循环)
#class Solution:
#    def addDigits(self,num):
#        while num>9:
#            c = 0
#            while num:
#                c += num % 10
#                num /= 10
#            num = c
#        return num

# ****************************************************************************
# 方法二：
class Solution:
    def addDigits(self,num):
        if num == 0:
            return 0
        return (num-1)%9+1



if __name__ == "__main__":
    aa = Solution()
    for i in xrange(1,30):
        print i,aa.addDigits(i)



