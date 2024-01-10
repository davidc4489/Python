def is_prime(nb):
    if nb < 2:
        return False
    
    for d in range(2, nb):
        if nb % d == 0:
            return False
    return True

def get_primes_list(inf, sup):
    primes_list = []
    for nb in range(inf, sup+1):
        if is_prime(nb):
            primes_list.append(nb)
    return primes_list