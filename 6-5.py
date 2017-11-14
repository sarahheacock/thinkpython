def gcd(a, b):
    if a%b == 0:
        return b
    if b%a == 0:
        return a
    if a > b:
        return gcd(b, a%b)
    return gcd(a, b%a)

print(gcd(12, 36))
print(gcd(36, 12))
print(gcd(8, 12))
print(gcd(12, 8))
