def narcissistic(value):
    v = str(value)
    power = len(v)
    v = list(v)
    v = [int(v) for v in v]
    return True if sum(num**power for num in v) == value else False
