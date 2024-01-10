def get_dividers(nb):
    dividers_list = []
    for i in range(1, nb+1):
        if nb % i == 0:
            dividers_list.append(i)
    return dividers_list