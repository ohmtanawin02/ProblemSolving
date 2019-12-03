import timeit

def reverse_slicing(s):
    return s[::-1]

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1 #appending chars in reverse order
    return s1

def reverse_while_loop(s):
    s1 =''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

def reverse_str_join(s):
    s1 = ''.join(reversed(s))
    return s1

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

def slicing_time():
    SETUP_CODE = '''
from __main__ import reverse_slicing
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_slicing(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
    print(times)
    print('Slicing time: {}'.format(min(times)))

def for_time():
    SETUP_CODE = '''
from __main__ import reverse_for_loop
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_for_loop(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
    print(times)
    print('for time: {}'.format(min(times)))

def while_time():
    SETUP_CODE = '''
from __main__ import reverse_while_loop
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_while_loop(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
    print(times)
    print('while time: {}'.format(min(times)))

def join_time():
    SETUP_CODE = '''
from __main__ import reverse_str_join
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_str_join(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
    print(times)
    print('join time: {}'.format(min(times)))

def list_time():
    SETUP_CODE = '''
from __main__ import reverse_list
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_list(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
    print(times)
    print('list time: {}'.format(min(times)))

def recursion_time():
    SETUP_CODE = '''
from __main__ import reverse_recursion
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_recursion(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
    print(times)
    print('recursion time: {}'.format(min(times)))

if __name__ == "__main__":
    slicing_time()
    for_time()
    while_time()
    join_time()
    list_time()
    recursion_time()