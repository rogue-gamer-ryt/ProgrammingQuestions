"""
The direct implementation of an inorder traversal using recursion has O(h) space comPlexity, where
h is the height of the tree. Recursion can be removed with an explicit stack, but the space complexity
remains O(h).

Write a nonrecursive program for computing the inorder traversal sequence for a binary tree.
Assume nodes have parent fields.
"""

# When we return to a parent if the just completed subtree was left child or right child.
# if left, we need to visit the parent and then traverse the right subtree
# if right, we compeleted traversing the parent
# we record the subtree's root before we move to the parent and then compare it with 
# the left child of parent

# Time complexity - o(n)
# Space complexity - o(1)
def inorder_traversal(tree):
    prev_node = None
    curr_node = tree
    result = []

    while curr_node:
        # If we are at the root or coming down from top
        if prev_node is None or prev_node == curr_node.parent:
            # Go inside the left subtree
            if curr_node.left is not None:
                next_node = curr_node.left
            else:
                # if not then we are at the root of the subtree
                result.append(curr_node.data)
                # Go back up
                next_node = curr_node.right if curr_node.right is not None else curr_node.parent
        
        # We came up to the curr node from its left child
        elif prev_node == curr_node.left:
            # Done with the left subtree
            result.append(curr_node.data)
            next_node = curr_node.right if curr_node.right is not None else curr_node.parent
        
        else:
            next_node = curr_node.parent
        
        prev_node = curr_node
        curr_node = next_node
    
    return result
    



