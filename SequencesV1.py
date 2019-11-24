import time

def SequencesV1(n):
    total = 0
    for i in range(n):
        total += (i+1)
    return(total)
n = int(input('input Value : '))

start = time.time()
print('answer :', SequencesV1(n))
print('time : ',(time.time()-start)*1000)