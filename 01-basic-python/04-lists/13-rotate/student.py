def rotate(xs, n):
    ys = xs[n:]
    zs = xs[:n]
    return ys + zs