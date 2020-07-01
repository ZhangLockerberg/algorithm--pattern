# 回溯法

## 背景

回溯法（backtrack）常用于遍历列表所有子集，是 DFS 深度搜索一种，一般用于全排列，穷尽所有可能，遍历的过程实际上是一个决策树的遍历过程。时间复杂度一般 O(N!)，它不像动态规划存在重叠子问题可以优化，回溯算法就是纯暴力穷举，复杂度一般都很高。

## 模板

```go
result = []
func backtrack(选择列表,路径):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        做选择
        backtrack(选择列表,路径)
        撤销选择
```

核心就是从选择列表里做一个选择，然后一直递归往下搜索答案，如果遇到路径不通，就返回来撤销这次选择。

## 示例

### [subsets](https://leetcode-cn.com/problems/subsets/)

> 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

遍历过程

![image.png](https://img.fuiboom.com/img/backtrack.png)

```Python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []
        
        route = []
        def backtrack(start, k):
            if len(route) == k:
                result.append(route.copy())
                return
            
            for i in range(start, n):
                route.append(nums[i])
                backtrack(i + 1, k)
                route.pop()

            return
        
        for k in range(n + 1):
            backtrack(0, k)
        
        return result
```

### [subsets-ii](https://leetcode-cn.com/problems/subsets-ii/)

> 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。说明：解集不能包含重复的子集。

```Python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        result = []
        
        route = []
        def backtrack(start, k):
            
            if len(route) == k:
                result.append(route.copy())
                return
            
            last = None
            for i in range(start, n):
                if nums[i] != last:
                    route.append(nums[i])
                    backtrack(i + 1, k)
                    last = route.pop()
            
            return
        
        for k in range(n + 1):
            backtrack(0, k)
        
        return result
```

### [permutations](https://leetcode-cn.com/problems/permutations/)

> 给定一个   没有重复   数字的序列，返回其所有可能的全排列。

思路 1：需要记录已经选择过的元素，满足条件的结果才进行返回，需要额外 O(n) 的空间

```Python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []
        
        in_route = [False] * n
        
        def backtrack(route=[]):
            
            if len(route) == n:
                result.append(route.copy())
                return
                
            for i in range(n):
                if not in_route[i]:
                    route.append(nums[i])
                    in_route[i] = True
                    backtrack()
                    route.pop()
                    in_route[i] = False
            
            return
        
        backtrack()
        return result
```

思路 2: 针对此题的更高级的回溯，利用原有的数组，每次回溯将新选择的元素与当前位置元素交换，回溯完成再换回来

```Python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []
        
        def backtrack(idx=0):
            if idx == n:
                result.append(nums.copy())
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            return

        backtrack()
        return result
```



### [permutations-ii](https://leetcode-cn.com/problems/permutations-ii/)

> 给定一个可包含重复数字的序列，返回所有不重复的全排列。

注意此题（貌似）无法使用上题的思路 2，因为交换操作会打乱排序。

```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        result = []
        
        in_route = [False] * n
        
        def backtrack(route=[]):
            
            if len(route) == n:
                result.append(route.copy())
                return
            
            last = None
            for i in range(n):
                if not in_route[i] and nums[i] != last:
                    route.append(nums[i])
                    in_route[i] = True
                    backtrack()
                    last = route.pop()
                    in_route[i] = False
            
            return
        
        backtrack()
        return result
```

## 练习

- [ ] [subsets](https://leetcode-cn.com/problems/subsets/)
- [ ] [subsets-ii](https://leetcode-cn.com/problems/subsets-ii/)
- [ ] [permutations](https://leetcode-cn.com/problems/permutations/)
- [ ] [permutations-ii](https://leetcode-cn.com/problems/permutations-ii/)

挑战题目

- [ ] [combination-sum](https://leetcode-cn.com/problems/combination-sum/)
- [ ] [letter-combinations-of-a-phone-number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
- [ ] [palindrome-partitioning](https://leetcode-cn.com/problems/palindrome-partitioning/)
- [ ] [restore-ip-addresses](https://leetcode-cn.com/problems/restore-ip-addresses/)
