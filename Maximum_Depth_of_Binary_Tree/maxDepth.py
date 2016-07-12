#!/usr/bin/env python
# encoding: utf-8

# 题目：给定一棵二叉树，找到它的最大深度
#       最大深度是指从根节点到最远的叶子节点的所经过的节点数
# 思路：递归

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归解法
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


