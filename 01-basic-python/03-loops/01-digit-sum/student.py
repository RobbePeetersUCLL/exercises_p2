def last_digit(n):
    return n%10

def remove_last_digit(n):
    return n//10

def digit_sum(n):
    total = 0
    i = len(str(n))
    while i > 0:
        total += last_digit(n)
        n = remove_last_digit(n)
        i -= 1
    return total