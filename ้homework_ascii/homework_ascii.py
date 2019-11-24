import time

def method1(msg):
    result = 0
    for i in msg :
        if i != " " :
            result = result + ord(i)
    return result

def method2(msg):
    result = 0
    for i in msg :
        if i == 'A' :
            result += 65
        if i == 'B' :
            result += 66
        if i == 'C' :
            result += 67
        if i == 'D' :
            result += 68
        if i == 'E' :
            result += 69
        if i == 'F' :
            result += 70
        if i == 'G' :
            result += 71
        if i == 'H' :
            result += 72
        if i == 'I' :
            result += 73
        if i == 'J' :
            result += 74
        if i == 'K' :
            result += 75
        if i == 'L' :
            result += 76
        if i == 'M' :
            result += 77
        if i == 'N' :
            result += 78
        if i == 'O' :
            result += 79
        if i == 'P' :
            result += 80
        if i == 'Q' :
            result += 81
        if i == 'R' :
            result += 82
        if i == 'S' :
            result += 83
        if i == 'T' :
            result += 84
        if i == 'U' :
            result += 85
        if i == 'V' :
            result += 86
        if i == 'W' :
            result += 87
        if i == 'X' :
            result += 88
        if i == 'Y' :
            result += 89
        if i == 'Z' :
            result += 90
    return result
    

def method3(msg):
    result = 0
    for i in msg.replace(' ','') :
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