def reverse_while_loop(s):
    s1 =''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

input_str = 'INE-KMUTNB'
if __name__ == '__main__':
    print('Reverse String using while loop =', reverse_while_loop(input_str))