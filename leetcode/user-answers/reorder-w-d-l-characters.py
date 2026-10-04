def solution(inputStr):
    count = {
        'W': 0,
        'D': 0,
        'L': 0
    }

    for ch in inputStr:
        count[ch] += 1

    output = []

    while count['W'] + count['D'] + count['L'] > 0:
        for ch in "WDL":
            if count[ch] > 0:
                output.append(ch)
                count[ch] -= 1

    return ''.join(output)
