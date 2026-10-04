def getMinLength(seq):
    length = 0

    for char in seq:
        if char == 'B' and length > 0:
            length -= 1
        else:
            length += 1

    return length
