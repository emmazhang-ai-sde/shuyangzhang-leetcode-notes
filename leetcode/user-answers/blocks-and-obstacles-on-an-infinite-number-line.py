from bisect import bisect_left, bisect_right


def solution(operations):
    # Collect every coordinate that may later contain an obstacle.
    positions = []

    for operation in operations:
        if operation[0] == 1:
            positions.append(operation[1])

    positions.sort()

    # Fenwick tree: records which obstacle positions have been activated.
    tree = [0] * (len(positions) + 1)

    def add(index):
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    def get_sum(index):
        total = 0

        while index > 0:
            total += tree[index]
            index -= index & -index

        return total

    result = []

    for operation in operations:
        if operation[0] == 1:
            x = operation[1]

            # Fenwick-tree indexes start at 1.
            index = bisect_left(positions, x) + 1
            add(index)

        else:
            x = operation[1]
            size = operation[2]

            left = x - size
            right = x - 1

            left_index = bisect_left(positions, left)
            right_index = bisect_right(positions, right)

            obstacle_count = (
                get_sum(right_index) - get_sum(left_index)
            )

            if obstacle_count == 0:
                result.append("1")
            else:
                result.append("0")

    return "".join(result)
