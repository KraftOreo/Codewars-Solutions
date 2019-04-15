def maxSequence(arr: list):
    s = 0
    max = 0
    if all([i > 0 for i in arr]):
        return sum(arr)
    elif all([i <= 0 for i in arr]):
        return 0
    else:
        for i in arr:
            s += i
            if s > max:
                max=s
            if s <= 0:
                s = 0
    return max