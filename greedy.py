import heapq

# 1. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 2. Prim's Minimal Spanning Tree Algorithm
class PrimMST:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.adj[u].append((w, v))
        self.adj[v].append((w, u))

    def prim_mst(self):
        min_heap = [(0, 0)]  # (weight, vertex)
        visited = set()
        mst_cost = 0

        while len(visited) < self.V:
            weight, current = heapq.heappop(min_heap)
            if current in visited:
                continue
            visited.add(current)
            mst_cost += weight
            for neighbor_weight, neighbor in self.adj[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_weight, neighbor))
        return mst_cost


# 3. Kruskal's Minimal Spanning Tree Algorithm
class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    def kruskal_mst(self):
        self.edges.sort()
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        mst_cost = 0

        for weight, u, v in self.edges:
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst_cost += weight
        return mst_cost


# 4. Dijkstra's Algorithm
def dijkstra(graph, src, V):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]  # (distance, vertex)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for weight, v in graph.get(u, []):
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist


# 5. Job Scheduling Problem
def job_scheduling(jobs):
    jobs.sort(reverse=True, key=lambda x: x[0])  # Sort by profit descending
    n = max(job[1] for job in jobs)
    slots = [-1] * n
    total_profit = 0

    for profit, deadline in jobs:
        for t in range(min(deadline, n) - 1, -1, -1):
            if slots[t] == -1:
                slots[t] = profit
                total_profit += profit
                break
    return total_profit


# Example Usage
if __name__ == "__main__":
    # 1. Selection Sort
    print("Selection Sort:")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Sorted:", selection_sort(arr))

    # 2. Prim's MST
    print("\nPrim's MST:")
    g1 = PrimMST(5)
    g1.add_edge(0, 1, 2)
    g1.add_edge(0, 3, 6)
    g1.add_edge(1, 2, 3)
    g1.add_edge(1, 3, 8)
    g1.add_edge(1, 4, 5)
    g1.add_edge(2, 4, 7)
    print("MST Cost:", g1.prim_mst())

    # 3. Kruskal's MST
    print("\nKruskal's MST:")
    g2 = KruskalMST(5)
    g2.add_edge(0, 1, 10)
    g2.add_edge(0, 2, 6)
    g2.add_edge(0, 3, 5)
    g2.add_edge(1, 3, 15)
    g2.add_edge(2, 3, 4)
    print("MST Cost:", g2.kruskal_mst())

    # 4. Dijkstra's Algorithm
    print("\nDijkstra's Algorithm:")
    graph = {
        0: [(4, 1), (1, 2)],
        1: [(1, 3)],
        2: [(2, 1), (5, 3)],
        3: []
    }
    print("Shortest Distances from Node 0:", dijkstra(graph, 0, 4))

    # 5. Job Scheduling Problem
    print("\nJob Scheduling Problem:")
    jobs = [(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]
    print("Maximum Profit:", job_scheduling(jobs))
