
a = 31415
b = 14142


def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)

    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

print(f'the greatest common divisor of {a} and {b} is {gcd(a, b)}')