def drop_nth(xs, n):
    ys = xs[:n]
    zs = xs[n+1:]
    return ys + zs