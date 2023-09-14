nombre = int(input("Saisir un nombre"))
string = input("Saisis une chaine de caractères")
if nombre == 0:
    print("Arrête ton cinéma")
elif any(i in string for i in 'aeiouy'):
    print(nombre)
elif (nombre)>= 42:
    print(nombre)
else: print(string) 

