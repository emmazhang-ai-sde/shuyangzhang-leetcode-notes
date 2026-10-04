# Chapter 4: DFS

## DFS 的适用范围

- Combination 组合问题：所有可能的组合
- Permutation 排列问题：所有可能的排列

## 使用 DFS 之前需要想清楚 3 问题

1. 函数与参数的定义
2. 递归的拆解
3. 递归的出口

## 题目

### Combinations
> Use `startIndex` to move forward only; no revisiting previous elements.

- [78. Subsets](https://leetcode.com/problems/subsets/description/)
- [90. Subsets II](https://leetcode.com/problems/subsets-ii/description/)
- [77. Combinations](https://leetcode.com/problems/combinations/description/)
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)
- [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/description/)
- [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/description/)
- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/)

### Permutations
> Iterate from the beginning each time; skip elements already in `temp`.

- [46. Permutations](https://leetcode.com/problems/permutations/description/)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/description/)

### Graph / Grid DFS
> Neither combinations nor permutations; search on a 2D grid or graph.

- [79. Word Search](https://leetcode.com/problems/word-search/description/)
- [733. Flood Fill](https://leetcode.com/problems/flood-fill/description/)
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/description/)

## DFS - Python 模板

```python
def dfs(self, candidates, temp, res, target, startIndex):
    if sum(temp) == target:
        res.append(temp + [])  # deepcopy
        return
    if sum(temp) > target:  # early terminate
        return
    for i in range(startIndex, len(candidates)):
        # 以 startIndex 对应数字开始
        num = candidates[i]
        temp.append(num)
        self.dfs(candidates, temp, res, target, i)  # i or i+1
        temp.pop(-1)
```

## DFS - Java 模板

```java
public void dfs(int[] candidates, int startIndex, List<Integer> temp,
                List<List<Integer>> res, int currSum, int target) {
    if (currSum == target) {
        res.add(new ArrayList<Integer>(temp)); // deepcopy
        return;
    }
    if (currSum > target) { // early terminate
        return;
    }
    for (int i = startIndex; i < candidates.length; i++) {
        int num = candidates[i];
        temp.add(num);
        dfs(candidates, i, temp, res, currSum + num, target);
        // 以 startIndex 对应数字开始
        temp.remove(temp.size() - 1);
    }
}
```
