# 题目清单 & 刷题建议

> 整理自算法课件第五期（密码jinli0531），按 Chapter 递进。每章包含：
> 1. **题目汇总**（按分类）
> 2. **推荐刷题顺序**（表格，含核心技巧 & 技术标签）

## Lyon · 高频考点 & 复习建议

答题收益率最高的考点，一般情况下就是这么几类：

1. **Binary Tree**  
   这是非常常见的。大家刷题时也知道，树的题目能考查的内容很多。它可以考 BFS（广度优先搜索），也可以考 DFS（深度优先搜索），能考查你对递归的理解。BFS 和 DFS 这两个方法广泛应用于所有的面试题型，包括图和列表。

2. **图论（Graph Theory）**  
   基本上只要考察，大概率就会有一道图类题。

3. **双指针（Two Pointers）**  
   这类方法用的也比较多。比如给你一个列表，或者像 Sliding Window（滑动窗口）这样的题目。它们不属于某种固定的算法，而是考查你对指针的理解。

4. **堆（Heap）+ Top K + 单调栈（Monotonic Stack）**  
   考查频率不算低。有些同学可能没用过单调栈解决实际问题，如果见到这类题完全不知道其特性，就没办法解题。所以单调栈是必须注意的常考题目。

5. **排序与区间（Sorted List / Intervals）**  
   比如这种题目：给定一个日程表，8点到10点有个会议，10点到11点有个会议，11点到13点有个会议，问你一共需要多少个会议室才能把这些会议安排好？这类题考得也比较多。

6. **前缀和（Prefix Sum）**  
   这也是一个常考类型。它通常不是考查的全部，而是作为解题的一部分，需要配合 HashMap 等其他数据结构联合使用。

7. **DP（动态规划）& Linked List** ⚠️ 低优先级  
   我的建议是可以放弃。虽然我们的算法课会讲面试中可能遇到的一维、二维 DP，但从面试复习的性价比来说，DP 和 Linked List 的考查频率在下降，不建议大家花太大功夫。

---

## Chapter 1 · Binary Search（二分法）

### 题目汇总

**套模板类型**
- [704. Binary Search](https://leetcode.com/problems/binary-search/)
- [702. Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)
- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

**OOXX 类型（找边界 / 分界）**
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

**二分答案类型**
- [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [1060. Missing Element in Sorted Array](https://leetcode.com/problems/missing-element-in-sorted-array/)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
- [774. Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/)
- [475. Heaters](https://leetcode.com/problems/heaters/)
- [1231. Divide Chocolate](https://leetcode.com/problems/divide-chocolate/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [704. Binary Search](https://leetcode.com/problems/binary-search/) | 套模板 | `start+1<end` 模板，避免死循环 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Binary Search</span>|
| 2 | [702. Search in Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) | 套模板 | 边界虚拟化，套同一模板 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Binary Search</span><br><span style="background:#f1f5f9;color:#475569;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Virtual Boundary</span>|
| 3 | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | 套模板 | 2D 矩阵展平为 1D 做二分 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Binary Search</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">2D Matrix</span>|
| 4 | [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | 套模板 | 从右上角出发，逐步排除行/列 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Two Pointers</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">2D Matrix</span>|
| 5 | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | OOXX | 找第一个 ≥ target 的位置 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">OOXX</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Boundary</span>|
| 6 | [34. Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | OOXX | 两次二分分别找左右边界 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">OOXX</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Boundary</span>|
| 7 | [278. First Bad Version](https://leetcode.com/problems/first-bad-version/) | OOXX | 判定函数直接映射 OOXX 模型 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">OOXX</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Boolean</span>|
| 8 | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) | OOXX | 比较 `a[mid]` 与 `a[mid+1]` 决定方向 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">OOXX</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Local Max</span>|
| 9 | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | OOXX | 比较 `mid` 与 `end` 判断旋转段 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">OOXX</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Rotated Array</span>|
| 10 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | OOXX | 两段都要判断，先确认有序侧 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">OOXX</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Rotated Array</span>|
| 11 | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) | 二分答案 | 最基础的二分答案，答案在 `[0, x]` |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Binary on Answer</span>|
| 12 | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 二分答案 | 构造判定函数，验证速度是否可行 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Binary on Answer</span><br><span style="background:#e0e7ff;color:#4338ca;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Feasibility Check</span>|
| 13 | [1060. Missing Element in Sorted Array](https://leetcode.com/problems/missing-element-in-sorted-array/) | 二分答案 | `missing(i) = nums[i] - nums[0] - i`，二分缺失计数 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Binary on Answer</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Count</span>|

---

## Chapter 2 · Binary Trees + Divide and Conquer

### 题目汇总

**Tree Traversal**
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**Tree DFS — Divide and Conquer**
- [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
- [112. Path Sum](https://leetcode.com/problems/path-sum/)
- [1120. Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/)
- [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Traversal | 认识三序遍历框架，最基础出发点 |<span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Traversal</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Preorder</span>|
| 2 | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Traversal | 中序 = BST 有序输出的基础 |<span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Traversal</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Inorder</span>|
| 3 | [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Traversal | 后序 = 先拿子结果再处理自己，D&C 前奏 |<span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Traversal</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Postorder</span>|
| 4 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | D&C | 第一道 D&C：返回值即深度，模板热身 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Return Value</span>|
| 5 | [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | D&C | 路径需要向下传参，体会 pass-down 写法 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Path</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pass-down</span>|
| 6 | [112. Path Sum](https://leetcode.com/problems/path-sum/) | D&C | 传参 + Boolean 返回值，判断叶节点触发 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Path</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Boolean</span>|
| 7 | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | D&C | 返回高度，用 -1 作哨兵表示不平衡 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Height</span><br><span style="background:#f1f5f9;color:#475569;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Sentinel</span>|
| 8 | [1120. Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/) | D&C | 返回 `(sum, count)` tuple，合并子结果 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Tuple Return</span>|
| 9 | [236. Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | D&C | 经典：返回值兼具"找到节点"与"路过节点"两层含义 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">LCA</span>|
| 10 | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | D&C | 传递 `(min, max)` 范围约束，BST 性质验证 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BST</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Range</span>|
| 11 | [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) | D&C | 返回 `(inc, dec)` tuple，合并递增/递减链 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Tuple Return</span>|
| 12 | [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | D&C | 原地修改树结构，后序 D&C 重接指针 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">D&C</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">In-place</span><br><span style="background:#f1f5f9;color:#475569;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pointer</span>|

---

## Chapter 3 · BFS + Topological Sorting

### 题目汇总

**BFS：Binary Tree 层级遍历**
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

**BFS：Topological Sort**
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)

**BFS + Heap：Dijkstra**
- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS Level Order | 队列模板，`size` 控制每层边界 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Queue</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Level Order</span>|
| 2 | [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | BFS Level Order | Level Order 变体，用奇偶层翻转方向 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Level Order</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Direction Toggle</span>|
| 3 | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS Level Order | 每层取队列最后一个元素 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Level Order</span>|
| 4 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Topological Sort | 构建 in-degree 数组 + 邻接表，BFS 逐层减度 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Topological Sort</span><br><span style="background:#e0e7ff;color:#4338ca;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">In-degree</span>|
| 5 | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra | Min Heap 贪心扩展，visited 防重复松弛 |<span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Dijkstra</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Greedy</span>|
| 6 | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Dijkstra | Dijkstra 加约束：state = `(cost, node, stops)`，多一维限制 |<span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Dijkstra</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Constraint</span>|

---

## Chapter 4 · DFS（深度优先搜索）

### 题目汇总

**Combinations（组合）**
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [77. Combinations](https://leetcode.com/problems/combinations/)
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [90. Subsets II](https://leetcode.com/problems/subsets-ii/)
- [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

**Permutations（排列）**
- [46. Permutations](https://leetcode.com/problems/permutations/)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/)

**Graph / Grid DFS**
- [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
- [79. Word Search](https://leetcode.com/problems/word-search/)
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1  | [78. Subsets](https://leetcode.com/problems/subsets/) | Combination | DFS 起点，无重复数字，最纯粹的子集枚举 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">startIndex</span>|
| 2  | [77. Combinations](https://leetcode.com/problems/combinations/) | Combination | `startIndex` 限定选择范围，固定大小 k |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">startIndex</span>|
| 3  | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Combination | 允许重复选：传 `i` 而非 `i+1` |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Reuse</span>|
| 4  | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) | Combination | 有重复数字 → 先排序，同层跳过重复 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Deduplication</span>|
| 5  | [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Combination | 去重剪枝 + 每个数只用一次 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Deduplication</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pruning</span>|
| 6  | [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Combination | 固定大小 k + 目标值，双重剪枝 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pruning</span>|
| 7  | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Combination | 多叉树 DFS，for 遍历字符集 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Multi-way</span>|
| 8  | [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/) | Combination | 树上 DFS，路径向下传参，叶节点触发收集 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Tree DFS</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pass-down</span>|
| 9  | [46. Permutations](https://leetcode.com/problems/permutations/) | Permutation | 每次从头枚举，`used[]` 跳过已选元素 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Used Array</span>|
| 10 | [47. Permutations II](https://leetcode.com/problems/permutations-ii/) | Permutation | 排列去重：排序后同层跳过 `candidates[i] == candidates[i-1]` |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Deduplication</span>|
| 11 | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Grid DFS | 2D Grid DFS 入门，四方向递归染色 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Grid DFS</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">4-Direction</span>|
| 12 | [79. Word Search](https://leetcode.com/problems/word-search/) | Grid DFS | Grid + Backtracking，访问后还原 `visited` |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Grid DFS</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span>|
| 13 | [212. Word Search II](https://leetcode.com/problems/word-search-ii/) | Grid DFS | Trie 剪枝优化，难度显著提升 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Grid DFS</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Trie</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pruning</span>|

---

## Chapter 5 · Graph（图）

### 题目汇总

**Graph Theory — BFS + DFS**
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
- [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

**BFS（图上最短路）**
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

**DFS / Backtracking**
- [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

**Topological Sort**
- [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

**Union Find**
- [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Graph Theory | 建邻接表 + BFS/DFS 数连通分量，图遍历基础模板 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Adjacency List</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Connected Components</span>|
| 2 | [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Graph Theory | 547 基础上加两条件：无环 + 全连通；`parent` 参数防回头 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Cycle Detection</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Connected</span>|
| 3 | [323. Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Union Find | 改用 Union Find 实现连通，与 BFS/DFS 对比 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Union Find</span>|
| 4 | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Graph Theory | DFS 遍历 + `visited` HashMap 映射 node → clone |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">DFS</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Node Copy</span>|
| 5 | [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | DFS | DAG 上 DFS 回溯，复用 Ch04 的 append/递归/pop 模板 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">DFS</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Backtracking</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">DAG</span>|
| 6 | [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Graph Theory | 先把二叉树重建为无向图，再 BFS 找距离 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Build Graph</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Tree</span>|
| 7 | [127. Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS | 隐式图（单词变换建边），BFS 求最短路；难度明显提升 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">BFS</span><br><span style="background:#f1f5f9;color:#475569;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Implicit Graph</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Shortest Path</span>|
| 8 | [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Topo Sort | 从单词顺序推导字符偏序关系，构建有向图 + Kahn 拓扑排序 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Topological Sort</span><br><span style="background:#e0e7ff;color:#4338ca;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">In-degree</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">DAG</span>|
| 9 | [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Topo Sort | Eulerian Path，Hierholzer 算法，与其他题完全不同范式 |<span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Eulerian Path</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hierholzer</span>|

---

## Chapter 6 · Two Pointer & Linked List

### 题目汇总

**Two Pointer — 同向（覆写/压缩）**
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Two Pointer — 同向（三色分区）**
- [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

**Two Pointer — 对撞（两端夹逼）**
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)

**Two Pointer — 设计 / HashMap**
- [170. Two Sum III — Data Structure Design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)

**区间合并**
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

**Linked List — 快慢指针** &nbsp;⚠️ *Lyon：Linked List 考查频率在下降，可降低复习优先级*
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

**Linked List — 操作**
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

**额外**
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)（归并/快排实现）

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | 同向双指针 | `fix` 记写入位，`k` 扫描，最简单的同向模板 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Same Direction</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Overwrite</span>|
| 2 | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | 同向双指针 | 同模板，换条件（值不同才写入） |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Same Direction</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Overwrite</span>|
| 3 | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | 同向双指针 | `fix` 扩展为两个边界指针，三色分区 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Same Direction</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Three-way Partition</span>|
| 4 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 区间合并 | 排序后线性扫描，贪心合并重叠区间 |<span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Sort</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Greedy</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Interval</span>|
| 5 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | 对撞双指针 | 排序后左右夹逼；HashMap 版学设计取舍 |<span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Collision</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 6 | [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) | 对撞双指针 | 固定最大边，对撞统计合法对数 |<span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Collision</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Count</span>|
| 7 | [170. Two Sum III](https://leetcode.com/problems/two-sum-iii-data-structure-design/) | 设计题 | `add` 频繁 → 用 HashMap；`find` 频繁 → 用 sorted list |<span style="background:#f1f5f9;color:#475569;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Design</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 8 | [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | 快慢指针 | slow 走 1 步，fast 走 2 步，最基础快慢指针 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Fast & Slow</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Linked List</span>|
| 9 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 快慢指针 | 同模板，fast 追上 slow 即有环 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Fast & Slow</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Cycle Detection</span>|
| 10 | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | 快慢指针 | 141 进阶：数学推导找入环口 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Fast & Slow</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Cycle Detection</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Math</span>|
| 11 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 链表操作 | 三指针迭代反转，基础但必须掌握 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Reverse</span><br><span style="background:#f1f5f9;color:#475569;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Pointer</span>|
| 12 | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | 链表操作 | 快慢找中点 + 反转后半段 + 对比，综合题 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Fast & Slow</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Reverse</span><br><span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Palindrome</span>|

---

## Chapter 7 · Heap + Top K + Monotonic Stack

### 题目汇总

**Heap（堆）**
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
- [767. Reorganize String](https://leetcode.com/problems/reorganize-string/)

**Top K Problems**
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

**Monotonic Stack（单调栈）**
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Top K | 维护大小为 k 的 MinHeap，堆顶即第 k 大 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Top K</span>|
| 2 | [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Top K | 词频统计 + 自定义比较器（频次相同按字典序） |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Top K</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Custom Comparator</span>|
| 3 | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap | 多路归并：每次从 k 个链表头取最小，Heap 维护 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">K-way Merge</span>|
| 4 | [378. Kth Smallest in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Heap | 多路归并变体，行视为有序链表 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">K-way Merge</span>|
| 5 | [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Heap | 多路归并 + 坐标 `(i, j)` 管理，去重入堆 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">K-way Merge</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Index Pair</span>|
| 6 | [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) | Heap | MaxHeap 贪心：每次取频率最高的两个字符交替填充 |<span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Max Heap</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Greedy</span>|
| 7 | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Mono Stack | 单调递减栈：栈顶被更大元素弹出时记录映射 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Monotonic Stack</span><br><span style="background:#e0e7ff;color:#4338ca;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Decreasing</span>|
| 8 | [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Mono Stack | 循环数组：遍历 `2n`，下标取模 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Monotonic Stack</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Circular Array</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Modulo</span>|
| 9 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Mono Stack | 同模板，弹出时直接记录距离（索引差） |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Monotonic Stack</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Index Distance</span>|
| 10 | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Heap | 双堆维护中位数（MaxHeap 左半 + MinHeap 右半），最难 |<span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Max Heap</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Median</span>|

---

## Chapter 8 · Sliding Window + Sweep Line

### 题目汇总

**Sliding Window**
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

**Sweep Line**
- [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding | 建立最基础的双指针框架 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Variable Window</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 2 | [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | Sliding | 套模板（具体版） |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Variable Window</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 3 | [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | Sliding | 套模板（泛化版） |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Variable Window</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 4 | [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding | 固定窗口 + 滑动更新 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Fixed Window</span><br><span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Frequency Array</span>|
| 5 | [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Sliding | 反向逻辑：求最短，收缩触发 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Variable Window</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Count</span>|
| 6 | [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Sliding | 每步累计答案数的计数技巧 |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Variable Window</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Count</span>|
| 7 | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding | 综合压轴：双 map 维护 need/have |<span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Variable Window</span><br><span style="background:#fee2e2;color:#b91c1c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Two Maps</span>|
| 8 | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Sliding | 单调队列独立数据结构技巧 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Fixed Window</span><br><span style="background:#e0e7ff;color:#4338ca;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Monotonic Deque</span>|
| 9 | [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Sweep | 区间排序基础 |<span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Sweep Line</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Sort</span>|
| 10 | [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Sweep | Heap 或事件排序两种解法 |<span style="background:#dcfce7;color:#15803d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Sweep Line</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Min Heap</span>|

---

## Chapter 9 · Prefix Sum + Stack + DP

### 题目汇总

**Prefix Sum**
- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

**Stack**
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

**DP** &nbsp;⚠️ *Lyon：DP 考查频率在下降，性价比不高，建议放低优先级*
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [91. Decode Ways](https://leetcode.com/problems/decode-ways/)

---

### 推荐刷题顺序

| # | 题目 | 分类 | 核心技巧 | 技术标签 |
|---|------|------|----------|----------|
| 1 | [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Prefix Sum | 最纯粹的 prefix sum，把模板背熟 |<span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Prefix Sum</span>|
| 2 | [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | Prefix Sum | prefix sum + HashMap，经典组合 |<span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Prefix Sum</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 3 | [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Prefix Sum | 把 0 当成 -1，转化成 325 的变体 |<span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Prefix Sum</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span>|
| 4 | [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Prefix Sum | prefix sum + 余数技巧 |<span style="background:#ccfbf1;color:#0f766e;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Prefix Sum</span><br><span style="background:#fef9c3;color:#a16207;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Hash Map</span><br><span style="background:#fce7f3;color:#be185d;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Modulo</span>|
| 5 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | 栈最基础的应用，热身 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Stack</span>|
| 6 | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) ⭐ | Stack | 先 Two Pointers，再 Stack 重做对比；三种解法均值得掌握 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Stack</span><br><span style="background:#dbeafe;color:#1d4ed8;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Two Pointers</span>|
| 7 | [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Stack | 难度跳升，不要跳过 #20 直接做 |<span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Stack</span>|
| 8 | [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | DP | 二维 DP，状态转移最直觉 |<span style="background:#e0e7ff;color:#4338ca;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">2D DP</span>|
| 9 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | DP | 一维 DP，最经典的 unbounded knapsack |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">1D DP</span>|
| 10 | [91. Decode Ways](https://leetcode.com/problems/decode-ways/) | DP | 一维 DP，边界条件多，放最后 |<span style="background:#ede9fe;color:#7c3aed;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">1D DP</span><br><span style="background:#ffedd5;color:#c2410c;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600;white-space:nowrap">Boundary</span>|

> **注意**：#42 Trapping Rain Water 是本章隐藏难题；#525 卡住时先回头看 #325，两题本质相同；DP 三题建议一两天内集中刷完。


## Chapter 10 · OOD
