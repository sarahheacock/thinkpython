def is_power(a, b):
    print(a, b)
    if a%b == 0:
        if a == b:
            return True
        return is_power(a/b, b)
    return False

print(is_power(8, 2))
