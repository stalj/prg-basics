def sum_reapeated_digits(n):
    sum = 0
    n_str = str(n)
    repeated = set()
    seen = set()
    for char in n_str:
        if char in seen:
            if char not in repeated:
                sum += int(char)*2
                repeated.add(char)
            else:
                sum += int(char)
        else:
            seen.add(char)
    return sum
    