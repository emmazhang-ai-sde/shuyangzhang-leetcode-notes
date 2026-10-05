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
