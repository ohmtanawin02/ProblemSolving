def main():
    Read()
    Calc()
    Print()
def Read():
    global Principal,Interest,Years,time
    Principal = float(input('Enter principal : '))
    Interest = float(input('Enter interest : '))
    Years = float(input('Enter years : '))
    time = float(input('Enter Number of time interest : '))
def Calc():
    global amount
    amount = Principal*(1 + Interest/time)**(Years*time)
def Print():
    print(amount)
main()
