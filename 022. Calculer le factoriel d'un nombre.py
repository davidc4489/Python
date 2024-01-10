def factorial(nb):
    product = 1
    for num in range(1, nb+1):
        product *= num

    return product

def recursion_factorial(nb):
    if nb==1:
        return 1
    return nb*recursion_factorial(nb-1)