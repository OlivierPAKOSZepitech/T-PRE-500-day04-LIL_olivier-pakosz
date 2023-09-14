nombre = 30
i = -30
while(i<= nombre):
    if(i % 3 == 0 and i % 5 == 0):
        print(str(i) + " FizzBuzz")
    elif(i % 3 == 0):
        print(str(i) + " Fizz")
    elif(i % 5 == 0):
        print(str(i) + " Buzz")
    
    else: print(i)
    i = i+1