# 最短路径问题

## Dijkstra's Algorithm

思想是 greedy 构造 shortest path tree (SPT)，每次将当前距离源点最短的不在 SPT 中的结点加入SPT，与构造最小生成树 (MST) 的 Prim's algorithm 非常相似。可以用 priority queue (heap) 实现。

### [network-delay-time](https://leetcode-cn.com/problems/network-delay-time/)

标准的单源最短路径问题，使用朴素的的 Dijikstra 算法即可，可以当成模板使用。

```Python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        # construct graph
        graph_neighbor = collections.defaultdict(list)
        for s, e, t in times:
            graph_neighbor[s].append((e, t))
        
        # Dijkstra
        SPT = {}
        min_heap = [(0, K)]
        
        while min_heap:
            delay, node = heapq.heappop(min_heap)
            if node not in SPT:
                SPT[node] = delay
                for n, d in graph_neighbor[node]:
                    if n not in SPT:
                        heapq.heappush(min_heap, (d + delay, n))
        
        return max(SPT.values()) if len(SPT) == N else -1
```

### [cheapest-flights-within-k-stops](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)

在标准的单源最短路径问题上限制了路径的边数，因此需要同时维护当前 SPT 内每个结点最短路径的边数，当遇到边数更小的路径 (边权和可以更大) 时结点需要重新入堆，以更新后继在边数上限内没达到的结点。

```Python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # construct graph
        graph_neighbor = collections.defaultdict(list)
        for s, e, p in flights:
            graph_neighbor[s].append((e, p))
        
        # modified Dijkstra
        prices, steps = {}, {}
        min_heap = [(0, 0, src)]
        
        while len(min_heap) > 0:
            price, step, node = heapq.heappop(min_heap)
            
            if node == dst: # early return
                return price

            if node not in prices:
                prices[node] = price
            
            steps[node] = step
            if step <= K:
                step += 1
                for n, p in graph_neighbor[node]:
                    if n not in prices or step < steps[n]:
                        heapq.heappush(min_heap, (p + price, step, n))
        
        return -1
```