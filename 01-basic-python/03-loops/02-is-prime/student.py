def is_prime(n):
    for m in range(2, n):
        if n % m == 0:
            return False

    return n > 1