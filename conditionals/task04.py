proposition = int(input("Donne moi un nombre "))

if(proposition == 42):
    print("OK")
elif(proposition <= 21):
    print("OK")
elif(proposition % 2):
    print("OK")
elif(proposition % 2 == 0 & proposition < 21):
    print("OK")
elif(proposition % 2 == False & proposition >= 45):
    print("OK")
else: print("You got wrong my poor friend")