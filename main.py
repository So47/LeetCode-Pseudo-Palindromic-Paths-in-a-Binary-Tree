# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def dfs(node, path):
            if not node:
                return 0
            # Toggle the bit corresponding to the node's value creating bitwise mask by left shifting one to node val position 
            path ^= 1 << node.val 

            # If it's a leaf node, check if the path can form a palindrome
            if not node.left and not node.right:
                # Check if path has at most one bit set
                if path & (path-1) == 0:
                    return 1
                else:
                    return 0    

            # Continue the DFS
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root,0)    
        
