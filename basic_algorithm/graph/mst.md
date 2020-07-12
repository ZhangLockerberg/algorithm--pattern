# 最小生成树

### [minimum-risk-path](https://www.lintcode.com/problem/minimum-risk-path/description)

> 地图上有 m 条无向边，每条边 (x, y, w) 表示位置 m 到位置 y 的权值为 w。从位置 0 到 位置 n 可能有多条路径。我们定义一条路径的危险值为这条路径中所有的边的最大权值。请问从位置 0 到 位置 n 所有路径中最小的危险值为多少？

**图森面试真题**。最小危险值为最小生成树中 0 到 n 路径上的最大边权。

```Python
# Kruskal's algorithm
class Solution:
    def getMinRiskValue(self, N, M, X, Y, W):
        
        # Kruskal's algorithm with union-find to construct MST
        parent = list(range(N + 1))
        
        def find(x):
            if parent[parent[x]] != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            else:
                return False
        
        edges = sorted(zip(W, X, Y))
        
        MST_edges = []        
        for edge in edges:
            if union(edge[1], edge[2]):
                MST_edges.append(edge)
            if find(0) == find(N):
                break
        
        MST = collections.defaultdict(list)
        target = find(0)
        for w, u, v in MST_edges:
            if find(u) == target and find(v) == target:
                MST[u].append((v, w))
                MST[v].append((u, w))
                
        # dfs to search route from 0 to n
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_w = dfs.pop()
            for n, w in MST[v]:
                cur_max_w = max(max_w, w)
                if n == N:
                    return cur_max_w
                if n != p:
                    dfs.append((n, v, cur_max_w))
```

```Python
# Prim's algorithm
class Solution:
    def getMinRiskValue(self, N, M, X, Y, W):
        
        # construct graph
        adj = collections.defaultdict(list)
        for i in range(M):
            adj[X[i]].append((Y[i], W[i]))
            adj[Y[i]].append((X[i], W[i]))
            
        # Prim's algorithm with min heap
        MST = collections.defaultdict(list)
        min_heap = [(w, 0, v) for v, w in adj[0]]
        heapq.heapify(min_heap)
        
        while N not in MST:
            w, p, v = heapq.heappop(min_heap)
            if v not in MST:
                MST[p].append((v, w))
                MST[v].append((p, w))
                for n, w in adj[v]:
                    if n not in MST:
                        heapq.heappush(min_heap, (w, v, n))
                
        # dfs to search route from 0 to n
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_w = dfs.pop()
            for n, w in MST[v]:
                cur_max_w = max(max_w, w)
                if n == N:
                    return cur_max_w
                if n != p:
                    dfs.append((n, v, cur_max_w))
```

