# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Problem Statement:
# 
# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
# Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.
# 
# Problem Difficulty: Medium


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        if (root1 and root2):
            if root1.val != root2.val:
                return False
            elif root1.left == None and root1.right == None and root2.left == None and root2.right == None and root1.val == root2.val:
                return True
            else:
                return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right))
        else:
            if not root1 and not root2:
                return True
            return False
