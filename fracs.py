def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def lcd(a, b):
    return a*b//gcd(a, b)


def add_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    den = lcd(den1, den2) 
    num1 *= den//den1
    num2 *= den//den2
    divider = gcd(num1+num2, den)
    return [(num1+num2)//divider, den//divider]


def sub_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    den = lcd(den1, den2) 
    num1 *= den//den1
    num2 *= den//den2
    divider = gcd(num1-num2, den)
    return [(num1-num2)//divider, den//divider]


def mul_frac(frac1, frac2): 
    num1, den1 = frac1
    num2, den2 = frac2
    num = num1*num2
    den = den1*den2
    return [num//gcd(num, den), den//gcd(num,den)]


def div_frac(frac1, frac2): 
    return mul_frac(frac1, [frac2[1], frac2[0]])


def is_positive(frac): 
    return frac[0]*frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    if frac2float(frac1) == frac2float(frac2):
        return 0 
    elif frac2float(frac1) < frac2float(frac2):
        return -1
    else:
        return 1


def frac2float(frac):
    return frac[0]/frac[1]
