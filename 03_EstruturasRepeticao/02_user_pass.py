usuario = senha = ''
while (usuario == senha):
    usuario = raw_input('Informe um nome de usuario: ')
    senha = raw_input('Informe a senha: ')
    if (usuario == senha):
        print 'A senha nao pode ser igual ao nome do usuario'

#outa forma de se fazer, quem sabe até melhor ;D
#while True:
#    nome = str(input("Nome [usuário]: ")).strip()
#    senha = str(input("Senha: "))
#    if nome == senha:
#        print("{:-^10}".format("ERRO"))
#        print("Você não pode adicionar como senha o seu nome.")
#    else:
#        print("_" * 30)
#        print(f"Cadastrado. Seja bem vindo {nome}.")
#        break
