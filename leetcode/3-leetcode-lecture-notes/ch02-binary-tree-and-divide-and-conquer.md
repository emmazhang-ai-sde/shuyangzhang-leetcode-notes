# Chapter 2: Binary Trees & Divide and Conquer

## 思路

分治和遍历，是**递归 Recursion**的两种不同形式

|  | Traversal | Divide & Conquer |
|--|-----------|------------------|
| 思路 | 当我到达这一层时，应该去做什么？向下传递的路线应该怎么走？应该传什么值去下一层？<br> 遍历的解法，一般都需要一个全局变量来记录我遍历之后的结果，如 max, min, list ... | 我的左儿子，右儿子得到返回值以后，我拿着左右儿子的结果，应该怎么做？<br>最核心点：**构造返回值** |
| **Top-down** | **preorder** — process node **first** | pass value **downward** as parameter |
| **Bottom-up** | **postorder** — process node **last** | return value **upward** to parent |
| Result carried by | global variable / parameter | **return value** |

## 题目

### Traversal & Basic

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

### Divide and Conquer

- [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/)
- [112. Path Sum](https://leetcode.com/problems/path-sum/description/)
- [1120. Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/description/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)
- [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)
- [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/)
- [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)

## Divide and Conquer - Python 模板

```python
def dfs(self, root):
    if not root:
        return 0

    leftReturn = self.dfs(root.left)
    rightReturn = self.dfs(root.right)

    # Optional leaf processing
    if root.left is None and root.right is None:
        ...

    height = max(leftReturn, rightReturn) + 1
    return height
```
