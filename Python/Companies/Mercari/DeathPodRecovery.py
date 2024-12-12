# Question: Pod Connectivity and Query Processing
# You are given a system of pods connected to each other, where some pods can write data to a database. The connections between the pods are represented as an array of edges, and there are queries to process the system's state. Your task is to process these queries and determine the appropriate outputs based on the state of the pods.

# Input:
# Connections: An array connections where each element is an edge [a, b], indicating that pod a is directly connected to pod b.

# All pods are connected directly or indirectly, meaning the graph is connected as a whole.
# Queries: An array queries where each query is of the form [type, pod]:

# type = 1: Check the status of the given pod. If the pod is not broken, return the pod number. If the pod is broken, return the lowest-numbered unbroken pod that is directly or indirectly connected to the queried pod. If no unbroken pods are connected, return -1.
# type = 2: Break the given pod, meaning it can no longer write to the database.
# Output:
# For each query of type = 1, output the result as described above in an array.

from collections import defaultdict

def build_components(graph, n):
    visited = [False] * (n + 1)
    components = {}
    current_component = 0

    def dfs(node):
        components[node] = current_component
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    for node in range(1, n + 1):
        if not visited[node]:
            current_component += 1
            dfs(node)

    return components

def process_pods(connections, queries, n):
    # Build adjacency list
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    
    # Find connected components
    components = build_components(graph, n)
    # Track broken pods
    broken = set()
    result = []

    for query in queries:
        if query[0] == 2:  # Break pod
            broken.add(query[1])
        elif query[0] == 1:  # Query for pod
            pod = query[1]
            if pod not in broken:
                result.append(pod)
            else:
                # Find all pods in the same component
                component_id = components[pod]
                candidates = [p for p in components if components[p] == component_id and p not in broken]
                if candidates:
                    result.append(min(candidates))
                else:
                    result.append(-1)
    return result

# Example usage
connections = [[1, 2], [2, 3], [3, 4], [1, 4]]
queries = [[2, 3], [1, 3], [2, 1], [1, 3]]
n = 4  # Total number of pods

output = process_pods(connections, queries, n)
print(output)  # Output: [1, 2]
