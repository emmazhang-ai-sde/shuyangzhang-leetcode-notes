def solution(lamps):
    diff = {}

    for x, r in lamps:
        left = x - r
        right = x + r

        diff[left] = diff.get(left, 0) + 1
        diff[right + 1] = diff.get(right + 1, 0) - 1

    points = sorted(diff)

    ans = 0
    active = 0
    prev = points[0]

    for point in points:
        if active == 1:
            ans += point - prev

        active += diff[point]
        prev = point

    return ans
