def main():
    n = int(input('Factorial : '))
    print(Fac(n))
def Fac(n):
    if n > 1 :
        Factorial = n * Fac(n-1)
    else :
        Factorial = 1
    return Factorial
main()