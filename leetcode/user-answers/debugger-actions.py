def solution(codeLength, breakpoints, actions):
    current_line = 1
    breakpoint_index = 0

    for action in actions:
        if action == "next":
            current_line += 1

        else:  # action == "continue"
            while breakpoints[breakpoint_index] <= current_line:
                breakpoint_index += 1

            current_line = breakpoints[breakpoint_index]

    return current_line
