def is_prime(nb):
    if nb < 2:
        return False
    
    for d in range(2, nb):
        if nb % d == 0:
            return False
    return True