# 第八章 Sliding Window + Sweep Line

## 题目列表

### Sliding Window

- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

### Sweep Line

- [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

---

## 概念

You are given an array on integers number and a positive integer k, count the number of contiguous subarrays having k duplicate pairs.

Eg.

```
[1, 2, 3, 2]    k = 2
```

---

## 代码模板

### Python

**Sliding Window**

```python
for j in range(len(s)):
    maps[s[j]] = maps.get(s[j], 0) + 1
    while maps[s[j]] > 1:
        maps[s[i]] -= 1
        i += 1
    ans = max(ans, j - i + 1)
return ans
```

**Sweep Line**

```python
times = []
for inter in intervals:
    times.append((inter[0], 1))
    times.append((inter[1], -1))
ans, count = 0, 0
times.sort()
for t in times:
    count += t[1]
    ans = max(ans, count)
return ans
```

### Java

**Sliding Window**

```java
for (int j = 0; j < s.length(); j++) {
    char lastChar = s.charAt(j);
    maps.put(lastChar, maps.getOrDefault(lastChar, 0) + 1);
    while (maps.get(lastChar) > 1) {
        char firstChar = s.charAt(i);
        maps.put(firstChar, maps.get(firstChar) - 1);
        i++;
    }
    ans = Math.max(ans, j - i + 1);
}
```

**Sweep Line**

```java
for (int j = 0; j < k.length(); j++) {
    maps.put(lastChar, maps.getOrDefault(lastChar, 0) + 1);
    while (maps.get(lastChar) > 1) {
        char firstChar = s.charAt(i);
        maps.put(firstChar, maps.get(firstChar) - 1);
        i++;
    }
    ans = Math.max(ans, j - i + 1);
}
```

---

## 例题

**Peak memory usage:**

For a series given server log file, get peak memory usage on the server.

Log file format: `ProdId, startTime, EndTime, Memory used`

```
1, 610, 820, 300
2, 710, 730, 400
```

Answer: 700 mb
