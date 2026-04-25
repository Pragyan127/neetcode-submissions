"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def clone(node):
            #“Mapping prevents duplicate nodes and avoids infinite loops by reusing already cloned nodes.”
            #“Seen before? Don’t clone again.”
            if node in oldtonew:
                return oldtonew[node]
            #Create empty clone
            copy = Node(node.val)
            #Store mapping
            oldtonew[node] = copy

            for nei in node.neighbors:
                #Fill neighbors (real cloning)
                copy.neighbors.append(clone(nei))
            return copy #The final return gives the starting node of the 
                        #fully constructed cloned graph.
        
        return clone(node) if node else None
        