#Depois de inserir um nome, atribuir SR e SRa.

def sexo(sex, nome):
    if sex == 1:
        return print(f'Ilmo Sr. {nome}')
    elif sex == 2:
        return print(f'Ilma Sra. {nome}')

def main ():
    print('Sexo: \n'
          'Masculino - digite 1\n'
          'Feminino - digite 2\n')
    nome = str(input('digite seu nome: '))
    sex = int(input('qual seu sexo: '))
    return sexo(sex, nome)

if __name__ == "__main__":
    main()
