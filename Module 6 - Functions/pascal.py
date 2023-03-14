def pascal(n):
    # Base condition to stop recursion
    if n == 1:
        return [[1]]

    # First entry of the new row is always 1
    new_row = [1]

    # Recurse triangle
    result = pascal(n - 1)

    # Grab the most recent row
    last_row = result[-1]

    # Now the magic happens per hint in the assignment document
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    # Last entry of the row is always 1
    new_row += [1]

    # Append results
    result.append(new_row)

    return result


if __name__ == '__main__':
    # Pascal recursion returns a list of list
    result = pascal(10)

    # Print!
    for list in result:
        print(*list, sep=" ")
