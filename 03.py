def sin(cor):
    if cor == "V":
        return print('Siga')
    elif cor == "A":
        return print('Atenção')
    else:
        return print('Pare')

def main():
    print('"V" - verde\n' 
    '"A"  - amarelo\n' 
    '"E" - vermelho')
    cor = str(input('digite uma letra: '))
    return sin(cor)

if __name__ == "__main__":
    main()
