# HackerRank OA Questions 1–2

## Question 1: Minimum Remaining String Length

### Problem

You are given a string `seq` made up only of the characters `'A'` and `'B'`.

You may repeatedly perform the following operation:

- Delete any occurrence of the substring `"AB"` or `"BB"`.
- After deletion, the remaining parts of the string are concatenated.

Your task is to determine the minimum possible length of the string after performing any number of valid deletions.

A substring refers to a contiguous sequence of characters.

Return the minimum remaining length.

### Example

```text
seq = "BABBA"
```

Output:

```text
1
```

Explanation:

```text
"BABBA"
   ↓ delete "AB"
" BBA"
   ↓ delete "BB"
" A"
```

The minimum remaining length is:

```text
1
```

### Best Algorithm

The key observation is that whenever the current character is `'B'` and there is already a remaining character before it, the two characters must form either:

```text
AB
```

or:

```text
BB
```

Both can be deleted.

Therefore, we only need to keep track of how many characters currently remain.

```python
def getMinLength(seq):
    length = 0

    for char in seq:
        if char == 'B' and length > 0:
            length -= 1
        else:
            length += 1

    return length
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

## Question 2: Maximum XOR Binary String

### Problem

You are given:

```text
bits
maxSet
x
```

where:

- `bits` is the length of the binary string.
- `x` is a binary string of length `bits`.
- `maxSet` is the maximum number of bits that may be set to `'1'` in another binary string `y`.

Construct a binary string `y` of the same length such that:

```text
x XOR y
```

is maximized.

The string `y` must satisfy:

- The number of `'1'` bits in `y` is at most `maxSet`.
- Leading zeros are allowed.

Return the binary string `y` that produces the maximum XOR value.

### Example

```text
bits = 3
x = "101"
maxSet = 1
```

Possible values of `y` containing at most one `'1'` include:

```text
000
001
010
100
```

Their XOR values are:

```text
000 XOR 101 = 101
001 XOR 101 = 100
010 XOR 101 = 111
100 XOR 101 = 001
```

The maximum result is:

```text
111
```

Therefore:

```text
y = "010"
```

### Best Algorithm

For each bit:

```text
x   y   XOR

0   0    0
0   1    1

1   0    1
1   1    0
```

Therefore:

- If `x[i] == '1'`, always choose `y[i] = '0'`.
- If `x[i] == '0'`, choosing `y[i] = '1'` makes the XOR bit equal to `1`.

However, `y` may contain at most `maxSet` ones.

Since the leftmost bits have the largest numerical value, we should place the available `1`s in `y` at the leftmost positions where `x[i] == '0'`.

This gives a greedy one-pass algorithm.

```python
def findYValue(bits, maxSet, x):
    y = []
    used = 0

    for ch in x:
        if ch == '0' and used < maxSet:
            y.append('1')
            used += 1
        else:
            y.append('0')

    return ''.join(y)
```

### Example Walkthrough

For:

```text
x = "101"
maxSet = 1
```

Process from left to right:

```text
x[0] = 1
→ y[0] = 0

x[1] = 0
→ use one available set bit
→ y[1] = 1

x[2] = 1
→ y[2] = 0
```

Therefore:

```text
x   = 101
y   = 010
XOR = 111
```

Answer:

```text
010
```

### Complexity

```text
Time:  O(bits)
Space: O(bits)
```

The `O(bits)` space is required to construct the returned string `y`. Excluding the output itself, the extra space is `O(1)`.