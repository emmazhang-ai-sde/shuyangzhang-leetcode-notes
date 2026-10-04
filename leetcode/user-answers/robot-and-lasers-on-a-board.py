def solution(numRows, numColumns, curRow, curColumn, laserCoordinates):
    dangerous_rows = set()
    dangerous_columns = set()

    for laser_row, laser_column in laserCoordinates:
        dangerous_rows.add(laser_row)
        dangerous_columns.add(laser_column)

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    max_safe_cells = 0

    for row_change, column_change in directions:
        # Start with the first cell after the protected initial cell.
        row = curRow + row_change
        column = curColumn + column_change
        safe_cells = 0

        while 1 <= row <= numRows and 1 <= column <= numColumns:
            if row in dangerous_rows or column in dangerous_columns:
                break

            safe_cells += 1
            row += row_change
            column += column_change

        max_safe_cells = max(max_safe_cells, safe_cells)

    return max_safe_cells
