import time
def ascii():    
    msg = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    counter = 0

    for x in msg :
        if x != " " :
            counter = counter + ord(x)

    print("\""+msg+"\"")
    print(" ASCII value of these texts is " + str(counter))
start = time.time()
ascii()
print('time :',(time.time()-start)*1000)
