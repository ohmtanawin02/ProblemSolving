import time

def method1(msg):
    result = 0
    for i in msg :
        if i != " " :
            result = result + ord(i)
    return result

def method2(msg):
    return sum(ord(i) for i in msg.replace(' ', ''))

def method3(msg):
    result = 0
    for i in msg.replace(' ', '') :
            result = result + ord(i)
    return result

msg = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
print("\""+msg+"\"")

start = time.time()
print(" answer of first method is " , method1(msg) , " #time = " ,(time.time()-start)*1000 , " milisecond.")
start = time.time()
print(" answer of second method is " , method2(msg) , " #time = " ,(time.time()-start)*1000 , " milisecond.")
start = time.time()
print(" answer of third method is " , method3(msg) , " #time = " ,(time.time()-start)*1000 , " milisecond.")