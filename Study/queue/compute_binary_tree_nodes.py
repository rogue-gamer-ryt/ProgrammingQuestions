"""
Given a binary tree, return an array consisting of the keys at the same level. Keys should appear
in the order of the corresponding nodes' depths, breaking ties from left to right. For example, you
should retum <<314>, <6,6>, <271,,561,2,271>, <28,0,3,1.,28>, <17,401.,257>, <641>> for the binary tree
"""

def binary_tree_depth_order(tree):
    result = []

    if not tree:
        return result
    
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = []
        
        for curr in curr_depth_nodes:
            for child in (curr.left, curr.right):
                if child:
                    nodes_to_consider.append(child)
        
        curr_depth_nodes = nodes_to_consider
        
        # curr_depth_nodes = [
        #     child
        #     for child in curr_depth_nodes for child in (curr.left, curr.right)
        #     if child
        # ]
    return result