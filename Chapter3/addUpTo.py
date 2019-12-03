import time

def addUpToV1(n):
    total = 0
    for i in range(n):
        total += (i+1)
    return(total)

def addUpToV2(n):
    return n * (n+1) /2
n = int(input('input Value : '))

start = time.time()
print('answer V1 :', addUpToV1(n))
print('time V1 : ',(time.time()-start)*1000)

start = time.time()
print('answer V2 :', addUpToV2(n))
print('time V2 :',(time.time()-start)*1000)
