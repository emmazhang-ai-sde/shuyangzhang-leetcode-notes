# Chapter 6: Two Pointer & LinkList

## Two Pointer 的适用范围

- 字符串操作 (in place)
- 线性操作 LinkedList, ArrayList, Substring 问题

## 明确 Two pointer 的几个问题：
- Fixed Pointer and Float Pointer 定义是什么
- 谁是 fixed pointer
- 谁是 float pointer，float pointer 如何移动

## 建议做题顺序

### Two Pointer

| 顺序 | 题目 | 要点 |
|------|------|------|
| 1 | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | 最简单的同向双指针，先建立 fix/k 的感觉 |
| 2 | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | 同一个模板，换个条件 |
| 3 | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | fix 变成两个，模板扩展 |
| 4 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 换了场景，但还是线性扫描的思路 |
| 5 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | 引入对撞 |
| 6 | [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) | 对撞的进阶应用 |
| 7 | [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) | 设计题，放最后 |

### Linked List

| 顺序 | 题目 | 要点 |
|------|------|------|
| 1 | [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | 最简单的快慢指针 |
| 2 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 同一个模板 |
| 3 | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | 141 的进阶 |
| 4 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 操作题，单独一类 |
| 5 | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | 综合题（快慢 + 反转） |

## 题目

### Two Pointer

#### ① 同向双指针 — 覆写/压缩
> 用 fix 记"下一个写入位"，用 k 扫描

- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

#### ② 同向双指针 — 三色分区
> fix 扩展到两个边界指针

- [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

#### ③ 对撞双指针 — 两端夹逼
> 排序后左右指针向中间收

- [1. Two Sum（排序版）](https://leetcode.com/problems/two-sum/)
- [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)

#### ④ 设计题 / HashMap
> 本质不是指针，是数据结构设计

- [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)
- [1. Two Sum（unsorted 版）](https://leetcode.com/problems/two-sum/)

#### ⑤ 区间合并
> 排序 + 贪心，双指针思维

- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

### Linked List

#### ⑥ 快慢指针
> slow 走 1 步，fast 走 2 步

- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

#### ⑦ 链表操作
> 纯反转 / 重组

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [234. Palindrome Linked List（反转后半段）](https://leetcode.com/problems/palindrome-linked-list/)

### 额外题目

- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) — 归并/快排实现，算法基础
