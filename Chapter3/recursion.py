def reverse_recursion(s):
    print(s)
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

input_str = 'INE-KMUTNB'
if __name__ == "__main__":
    print('Reverse String using recursive =', reverse_recursion(input_str))