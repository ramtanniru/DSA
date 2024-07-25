from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for child in node.neighbors:
                copy.neighbors.append(dfs(child))
            return copy 
        oldToNew = dict()
        return dfs(node) if node else None 