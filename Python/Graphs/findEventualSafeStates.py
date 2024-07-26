class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def topoSort(adj,V):
            inDegree = [0 for i in range(V)]
            queue = deque([])
            for children in adj.values():
                for node in children:
                    inDegree[node] += 1
            for i,x in enumerate(inDegree):
                if x==0:
                    queue.append(i)
            res = []
            while queue:
                node = queue.popleft()
                res.append(node)
                for child in adj[node]:
                    inDegree[child] -= 1
                    if inDegree[child]==0:
                        queue.append(child)
            return res
        # reversing the nodes 
        reversedGraph = defaultdict(list)
        V = len(graph)
        for parent,children in enumerate(graph):
            for child in children:
                reversedGraph[child].append(parent)
        for i in range(V):
            if i not in reversedGraph:
                reversedGraph[i] = []
        print(reversedGraph)
        return sorted(topoSort(reversedGraph,V)) 
                
                