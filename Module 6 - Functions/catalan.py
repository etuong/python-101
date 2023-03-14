def catalan(n: int, k: int):
    # Each recursion has this mathematical formula
    result = (n + k) / k

    # Base condition, recurse if k is less than n
    if k < n:
        # Concatenate by multiplying to the previous recursion
        result *= catalan(n, k + 1)

    return result


if __name__ == '__main__':
    for p in range(2, 16):
        x = catalan(p, 2)
        print(f"Order {p} Catalan number = {int(x)}")
