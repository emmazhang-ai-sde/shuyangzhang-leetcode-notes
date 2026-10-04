# 第九章 Prefix Sum + Stack + DP

## 概念

`List[1, 3, 5, 8, 9]` — 计算某一 j 之间的 sum

参考：https://leetcode.com/problems/continuous-subarray-sum/

```
sum(j) = presum[j] - presum[i-1]
prefixArr[] = {-2, -3, 1, -4, -2, -3}
```

---

## 题目列表

### Prefix Sum

- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

### Stack

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

### DP

- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- [91. Decode Ways](https://leetcode.com/problems/decode-ways/)

---

## 例题

小偷去偷东西，给定一个 int 数组，第 i 天和 time 天内每天安保数量递减，第 i 天到第 j 天 security 减少，比如输入 security `[5, 3, 3, 4, 6]`，time=2，输出 `[4]`

```
0 1 2 3 0
0 4 3 2 0
```

---

## 代码模板

### Python - Prefix Sum

```python
self.prefix = [0] * (len(nums) + 1)
for i, val in enumerate(nums):
    self.prefix[i+1] = self.prefix[i] + val
return self.prefix[right+1] - self.prefix[left]
```

### Java - Prefix Sum

```java
int[] prefix = new int[nums.length + 1];
Arrays.fill(prefix, 0);
for (int i = 0; i < nums.length; i++) {
    prefix[i+1] = prefix[i] + nums[i];
}
return prefix[right + 1] - prefix[left];
```
