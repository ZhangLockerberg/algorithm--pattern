# 最小生成树

### [minimum-risk-path](https://www.lintcode.com/problem/minimum-risk-path/description)

> 地图上有 m 条无向边，每条边 (x, y, w) 表示位置 m 到位置 y 的权值为 w。从位置 0 到 位置 n 可能有多条路径。我们定义一条路径的危险值为这条路径中所有的边的最大权值。请问从位置 0 到 位置 n 所有路径中最小的危险值为多少？

**图森面试真题**。最小危险值为最小生成树中 0 到 n 路径上的最大边权。

```Python
# Kruskal's algorithm
class Solution:
    def getMinRiskValue(self, n, m, x, y, w):
        
        # Kruskal's algorithm with union-find to construct MST
        parent = list(range(n + 1))
        
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
        
        edges = sorted(zip(x, y, w), key=lambda x: x[2])
        
        mst_edges = []        
        for edge in edges:
            if union(edge[0], edge[1]):
                mst_edges.append(edge)
            if find(0) == find(n):
                break
        
        mst = collections.defaultdict(list)
        target = find(0)
        for u, v, r in mst_edges:
            if find(u) == target and find(v) == target:
                mst[u].append((v, r))
                mst[v].append((u, r))
                
        # dfs to search route from 0 to n
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_risk = dfs.pop()
            for a, r in mst[v]:
                cur_max = max(max_risk, r)
                if a == n:
                    return cur_max
                if a != p:
                    dfs.append((a, v, cur_max))
```

```Python
# Prim's algorithm
class Solution:
    def getMinRiskValue(self, n, m, x, y, w):
        
        # construct graph
        adj = collections.defaultdict(list)
        for i in range(m):
            adj[x[i]].append((y[i], w[i]))
            adj[y[i]].append((x[i], w[i]))
            
        # Prim's algorithm with min heap
        mst = collections.defaultdict(list)
        min_heap = [(r, 0, v) for v, r in adj[0]]
        heapq.heapify(min_heap)
        
        while n not in mst:
            r, u, v = heapq.heappop(min_heap)
            if v not in mst:
                mst[u].append((v, r))
                mst[v].append((u, r))
                for nei, w in adj[v]:
                    if nei not in mst:
                        heapq.heappush(min_heap, (w, v, nei))
                
        # dfs to search route from 0 to n
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_risk = dfs.pop()
            for a, r in mst[v]:
                cur_max = max(max_risk, r)
                if a == n:
                    return cur_max
                if a != p:
                    dfs.append((a, v, cur_max))
```

