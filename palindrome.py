def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    temp = word

    while len(temp) > 0:
        if last(temp) != first(temp):
            return False
        temp = middle(temp)

    return True

print(is_palindrome('racecar'))
print(is_palindrome('race'))
