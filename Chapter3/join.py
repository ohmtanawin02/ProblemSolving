def reverse_str_join(s):
    s1 = ''.join(reversed(s))
    return s1

input_str = 'INE-KMUTNB'
if __name__ == "__main__":
    print('Reverse String using string join =', reverse_str_join(input_str))