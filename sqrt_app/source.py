import cmath, math


def sqrt(n, eps):
    try:
        n = float(n)
    except ValueError:
        n = n.replace(',', '.')
        try:
            n = float(n)
        except ValueError:
            return "NaN"
    if n > 0:
        res = round(math.sqrt(n), eps)
        if res - int(res) == 0:
            res = int(res)
        return [f"{res}", f"{-res}"]
    elif n < 0:
        res = round(cmath.sqrt(n).imag, eps)
        if res - int(res) == 0:
            res = int(res)
        return [f"{res}i", f"{-res}i"]
    else:
        return n


#while True:
#    eps = int(input('Точность: '))
#    num = input('Число: ')
#    sqrt(num, eps)
