def prime_num(n):
    prime_list = []
    if n < 1:
        return 'Input should be positive'
    candidate = 2

    while len(prime_list) < n:
        is_prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(candidate)
        candidate += 1
    return prime_list[-1]