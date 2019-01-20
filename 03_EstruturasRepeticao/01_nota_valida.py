nota = -1
while (nota < 0) or (nota > 10):
    nota = int(raw_input('Informe uma nota: '))
    if (nota < 0) or (nota > 10):
        print 'Nota Invalida'

# outro jeito de se fazer: (quem sabe até melhor ;D )
#while True:
#    nota =  int(input("Informe uma nota [de 0 a 10]: "))
#    if nota < 0 or nota > 10:
#        print("Tente novamente.")
#    else:
#        print(f"Nota informada: {nota}")
#        break
