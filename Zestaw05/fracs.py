import math

def add_frac(frac1, frac2):
    frac1 = safe_check(frac1)
    frac2 = safe_check(frac2)
    frac1, frac2 = make_common_denominator(frac1, frac2)
    return simplify([frac1[0] + frac2[0], frac1[1]])

def sub_frac(frac1, frac2):
    frac1 = safe_check(frac1)
    frac2 = safe_check(frac2)
    frac1, frac2 = make_common_denominator(frac1, frac2)
    return simplify([frac1[0] - frac2[0], frac1[1]])

def mul_frac(frac1, frac2):
    frac1 = safe_check(frac1)
    frac2 = safe_check(frac2)
    return simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):
    frac1 = safe_check(frac1)
    frac2 = safe_check(frac2)
    if(is_zero(frac2)):
        raise NameError("Mianownik nie moze byc 0")
    return simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):
    frac = safe_check(frac)
    return frac[0] > 0

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2): # frac1 > frac2 = 1, frac1 < frac2 = -1, frac1 == frac2 = 0
    frac1 = safe_check(frac1)
    frac2 = safe_check(frac2)
    frac1, frac2 = make_common_denominator(frac1, frac2)
    if frac1[0] > frac2[0]:
        return 1
    elif frac1[0] < frac2[0]:
        return -1
    elif frac1[0] == frac2[0]:
        return 0

def frac2float(frac):
    frac = safe_check(frac)
    return float(frac[0] / frac[1])

def simplify(frac):
    if is_zero(frac):
        return [0, 1]
    if((frac[0] > 0 and frac[1] < 0) or (frac[0] < 0 and frac[1] < 0)):
        frac[0] = -1 * frac[0]
        frac[1] = -1 * frac[1]
    common_divisor = math.gcd(int(frac[0]), int(frac[1]))
    if common_divisor == 1:
        return frac
    else:
        return [int(frac[0] / common_divisor), int(frac[1] / common_divisor)]

def zero_in_denominator(frac):
    if frac[1] == 0:
        raise NameError("Mianownik nie moze byc 0")

def safe_check(frac):
    zero_in_denominator(frac)
    return simplify(frac)

def make_common_denominator(frac1, frac2):
    denominator1 = frac1[1]
    denominator2 = frac2[1]
    frac1 = [frac1[0] * denominator2, frac1[1] * denominator2]
    frac2 = [frac2[0] * denominator1, frac2[1] * denominator1]
    return frac1, frac2
