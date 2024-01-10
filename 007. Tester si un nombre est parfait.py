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