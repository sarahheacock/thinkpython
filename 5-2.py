# Fermat's Last Theorem says that there are no positive integers

def fermat():
    a = int(raw_input('a: positive integer\n'))
    if a < 1:
        print('a needs to be greater than 0')
    else :
        b = int(raw_input('b: positive integer\n'))
        if b < 1:
            print('b needs to be greater than 0')
        else :
            c = int(raw_input('c: positive integer\n'))
            if c < 1:
                print('c needs to be greater than 0')
            else :
                n = int(raw_input('n: positive integer greater than 2\n'))
                if n <= 2:
                    print('n needs to be greater than 2')
                else :
                    test = a**n + b**n != c**n
                    if test:
                        print('No, that doesnt work.')
                    else :
                        print('Holy smokes, Fermat was wrong!')

fermat()
