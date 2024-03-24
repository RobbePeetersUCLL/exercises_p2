def median(ns):
    sorted_ns = sorted(ns)

    if len(sorted_ns) % 2 == 0:
        x = len(sorted_ns) // 2 
        return (sorted_ns[x] + sorted_ns[x-1]) / 2
    else:
        x = len(sorted_ns) // 2
        return sorted_ns[x]