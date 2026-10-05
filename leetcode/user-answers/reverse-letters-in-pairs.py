def solution(s):
    chars = list(s)

    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]

    return "".join(chars)
