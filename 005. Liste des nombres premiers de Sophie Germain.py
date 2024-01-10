def is_prime(nb):
    if nb < 2:
        return False
    
    for d in range(2, nb):
        if nb % d == 0:
            return False
    return True

def is_prime_SG(nb):
    if (is_prime(nb) & is_prime((nb*2)+1)):
        return True
    else:
        return False
    
def get_primes_SG_list(inf, sup):
    primes_SG_list = []
    for nb in range (inf, sup+1):
        if is_prime_SG(nb):
            primes_SG_list.append(nb)
    return primes_SG_list