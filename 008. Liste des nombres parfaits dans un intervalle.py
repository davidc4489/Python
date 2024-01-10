def get_dividers(nb):
    dividers_list = []
    for i in range(1, nb+1):
        if nb % i == 0:
            dividers_list.append(i)
    return dividers_list

def is_perfect(nb):
    if sum(get_dividers(nb)[:-1]) == nb:
        return True
    else:
        return False
    
def get_perfect_list(inf, sup):
    perfect_list = []
    for nb in range(inf, sup+1):
        if is_perfect(nb):
            perfect_list.append(nb)
    return perfect_list