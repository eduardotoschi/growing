def ehPrimo(n):
    if (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    else:
        i = 3
        while (i <= (n / i)):
            if ((n % i) == 0):
                return False
            i += 2
        return True

    return False

def maior_primo(n):

    if (n < 2):
        return 0
    elif (n == 2):
        return 2
    else:
        
        while (n > 2):
            if (ehPrimo(n)):
                return n
            n -= 1
        return n

    return 0