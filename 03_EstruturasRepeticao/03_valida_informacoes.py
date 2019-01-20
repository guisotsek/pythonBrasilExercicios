# Validacao do nome, melhorado.
while True:
    while True:
        nome = str(input("Nome: ")).strip()
        if len(nome) <= 3:
            print("Nome inválido, ele deve ter mais de 3 letras. Tente novamente.")
        else:
            break
    while True:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 150:
            print("Idade válida apenas entre 0 e 150. Tente novamente.")
        else:
            break
    while True:
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if sexo not in "FM":
            print("Sexo inválido, válido apenas se M(masculino) ou F(feminino). Tente novamente")
        else:
            break
    while True:
        sal = float(input("Salário: R$"))
        if sal == 0:
            print("Salário inválido, ele deve ser maior que zero(0). Tente novamente.")
        else:
            break
    while True:
        est_civil = str(input("Estado civil [S/C/V/D]: ")).strip().upper()[0]
        if  est_civil not in "SCVD":
            print("Estado civil inválido. Tente novamente.")
        else:
            break
    break
