# 深度优先搜索，广度优先搜索

### 深度优先搜索模板

- 先序，递归

```Python
def DFS(x):
    visit(x)
    for n in neighbor(x):
        if not visited(n):
            DFS(n)
    return
```

- 先序，迭代

```Python
def DFS(x):
    dfs = [x] # implement by a stack
    while dfs:
        v = dfs.pop()
        if not visited(v):
            visit(v)
            
            for n in neighbor(v):
                if not visited(n):
                    dfs.append(n)
    return
```

- 后序，递归

```Python
def DFS(x): # used when need to aggregate results from children
    discovering(x)
    for n in neighbor(x):
        if not discovering(n) and not visited(n):
            DFS(n)
    visit(x)
    return
```

### 广度优先搜索模板

相对于 dfs 可能收敛更慢，但是可以用来找不带权的最短路径

- 以结点为单位搜索

```Python
def BFS(x):
    bfs = collections.deque([x])
    while bfs:
        v = bfs.popleft()
        if not visited(v):
            visit(v)
            for n in neighbor(v):
                if not visited(v):
                    bfs.append(n)
    return
```

- 以层为单位搜索，典型应用是找不带权的最短路径

```Python
def BFS(x):
    bfs = collections.deque([x])
    while bfs:
        num_level = len(bfs)
        for _ in range(num_level)
            v = bfs.popleft()
            if not visited(v):
                visit(v)
                for n in neighbor(v):
                    if not visited(v):
                        bfs.append(n)
    return
```

## 例题

### [shortest-bridge](https://leetcode-cn.com/problems/shortest-bridge/)

> 在给定的 01 矩阵 A 中，存在两座岛 (岛是由四面相连的 1 形成的一个连通分量)。现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。返回必须翻转的 0 的最小数目。
>

**图森面试真题**。思路：DFS 遍历连通分量找边界，从边界开始 BFS找最短路径

```Python
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        M, N = len(A), len(A[0])
        
        for i in range(M):
            for j in range(N):
                if A[i][j] == 1: # start from a 1
                    dfs = [(i, j)]
                    break

        bfs = collections.deque([])
                    
        while dfs:
            r, c = dfs.pop()
            if A[r][c] == 1:
                A[r][c] = -1
                        
                if r - 1 >= 0:
                    if A[r - 1][c] == 0: # meet and edge
                        bfs.append((r - 1, c))
                    elif A[r - 1][c] == 1:
                        dfs.append((r - 1, c))

                if r + 1 < M:
                    if A[r + 1][c] == 0:
                        bfs.append((r + 1, c))
                    elif A[r + 1][c] == 1:
                        dfs.append((r + 1, c))
                                
                if c - 1 >= 0:
                    if A[r][c - 1] == 0:
                        bfs.append((r, c - 1))
                    elif A[r][c - 1] == 1:
                        dfs.append((r, c - 1))
                        
                if c + 1 < N:
                    if A[r][c + 1] == 0:
                        bfs.append((r, c + 1))
                    elif A[r][c + 1] == 1:
                        dfs.append((r, c + 1))
        flip = 1
        while bfs:
            num_level = len(bfs)
            for _ in range(num_level):
                r, c = bfs.popleft()
                if A[r][c] == 0:
                    A[r][c] = -2
                                
                    if r - 1 >= 0:
                        if A[r - 1][c] == 0:
                            bfs.append((r - 1, c))
                        elif A[r - 1][c] == 1:
                            return flip

                    if r + 1 < M:
                        if A[r + 1][c] == 0:
                            bfs.append((r + 1, c))
                        elif A[r + 1][c] == 1:
                            return flip
                                
                    if c - 1 >= 0:
                        if A[r][c - 1] == 0:
                            bfs.append((r, c - 1))
                        elif A[r][c - 1] == 1:
                            return flip
                        
                    if c + 1 < N:
                        if A[r][c + 1] == 0:
                            bfs.append((r, c + 1))
                        elif A[r][c + 1] == 1:
                            return flip
            flip += 1
```

