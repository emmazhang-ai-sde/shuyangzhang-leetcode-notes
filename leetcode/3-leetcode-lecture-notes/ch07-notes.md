# 第七章 Heap + TOP k + Monotonic Stack

## 知识点总结

### Heap 解决的问题
- 从 N 个数找最大/最小的数
- Push, Pop O(LGN)
- Peek O(1)

### TOPK 问题
从 N 个数找第 K 大的数 / 第 K 小的数
（第 K 大则用 MinHeap，反之则用 maxHeap）

### 单调栈问题
- **单调递增栈**：在 O(N) 的时间复杂度内，找到第一个比当前元素小的值
- **单调递减栈**：在 O(N) 的时间复杂度内，找到第一个比当前元素大的值

---

## 题目列表

### Heap 相关
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
- [767. Reorganize String](https://leetcode.com/problems/reorganize-string/)

### Top K Problems
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

### Mono Stack
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

---

## Python 模板

### Heap PYTHON 模板

```python
maps = {}

for i in words:
    maps[i] = maps.get(i, 0) + 1

heap = []

for word, count in maps.items():
    heapq.heappush(heap, Item(count, word))
    if len(heap) > k:
        heapq.heappop(heap)
```

### Mono Stack PYTHON 模板

```python
stack = []
maps = {}

for index, num in enumerate(nums):
    while stack and num > nums[stack[-1]]:
        key = stack.pop()
        maps[key] = index
    stack.append(index)
```

---

## Java 模板

### Heap Java 模板

```java
PriorityQueue<Item> pq = new PriorityQueue<>((x1, x2) -> {
    if (x1.freq == x2.freq) {
        return x2.word.compareTo(x1.word);
    }
    return Integer.compare(x1.freq, x2.freq);
});

HashMap<String, Integer> freq = new HashMap<>();
for (String word : words) {
    freq.put(word, freq.getOrDefault(word, 0) + 1);
}
for (Map.Entry<String, Integer> entry : freq.entrySet()) {
    Item item = new Item(entry.getValue(), entry.getKey());
    pq.add(item);
    if (pq.size() > k) {
        pq.poll();
    }
}
```

### Mono Stack Java 模板

```java
Deque<Integer> stack = new ArrayDeque<>();

for (int i = 0; i < nums2.length; i++) {
    while (!stack.isEmpty() && nums2[stack.peek()] < nums2[i]) {
        int key = stack.pop();
        maps.put(key, i);
    }
    stack.push(i);
}
```