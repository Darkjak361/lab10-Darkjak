
# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline:
    #   1. Create an empty stack.
    #   2. Go through each token in the list.
    #   3. If the token is a number, convert it to an integer and push it.
    #   4. If the token is an operator, pop the last two numbers.
    #   5. Perform the calculation and push the result.
    #   6. Return the final number in the stack.

    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack.pop()


def decode_string(s):
    # Outline:
    #   1. Create a stack to store previous strings and repeat counts.
    #   2. Go through each character in the string.
    #   3. If it is a number, build the repeat count.
    #   4. If it is an opening bracket, save the current string and count.
    #   5. If it is a closing bracket, repeat the current string.
    #   6. Return the decoded string.

    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)

        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0

        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = previous_string + current_string * repeat_count

        else:
            current_string += char

    return current_string


def daily_temperatures(temps):
    # Outline:
    #   1. Create a result list filled with zeros.
    #   2. Create a stack to store days waiting for warmer temperatures.
    #   3. Go through each temperature.
    #   4. While the current temperature is warmer than the temperature
    #      at the top of the stack, remove that day.
    #   5. Calculate how many days passed and store the answer.
    #   6. Push the current day onto the stack.
    #   7. Return the result list.

    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   1. Check if the grid is empty.
    #   2. Create a visited set to remember land already explored.
    #   3. Go through every position in the grid.
    #   4. If an unvisited land cell is found, increase the island count.
    #   5. Use a stack to explore connected land cells.
    #   6. Check the four directions: up, down, left, and right.
    #   7. Mark explored cells as visited so they are not counted again.
    #   8. Return the number of islands.

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1

                stack = [(r, c)]
                visited.add((r, c))

                while stack:
                    row, col = stack.pop()

                    directions = [
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1)
                    ]

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (0 <= new_row < rows and
                            0 <= new_col < cols and
                            grid[new_row][new_col] == "1" and
                            (new_row, new_col) not in visited):

                            visited.add((new_row, new_col))
                            stack.append((new_row, new_col))

    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
