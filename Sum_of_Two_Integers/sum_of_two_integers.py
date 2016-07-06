#!/usr/bin/env python
# encoding: utf-8

# 题目：给定两个数a和b, 求它们的和。要求不使用“+”和“-”运算符
# 思路：首先要知道，异或也被称为“模2和”，所以这题就是运用异或的位运算啦~
#       我们可以每次取最低位来计算，然后每次右移一位。
# 注意：1. 进位为两个数字1
#       2. 负数情况下，右移最高位补的是1，因此值得注意要取到什么时候为止。


# *****************************************************************************
# java的解法更简单
# java

#public class Solution{
#    public int getSum(int a, int b){
#        while (b != 0){
#            int c = a & b;   // carry
#            a ^= b;          // add
#            b = c << 1;
#        }
#        return a;
#    }
#}



# *****************************************************************************
# python解法 (32位，64位中这种方法是不行的)

class Solution(object):
    def getSum(self, a, b):
        """
        :type a : int
        :type b : int
        :rtype : int
        """
        MOD = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a = (a^b)&MOD
            b = ((a&b)<<1)&MOD
        return a if a <= MAX_INT else (a&MAX_INT)-MAX_INT-1

if __name__ == "__main__":
    aaa = Solution()
    print aaa.getSum(1,2)
