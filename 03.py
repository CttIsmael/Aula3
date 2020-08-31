def sin(cor):
    if cor.upper() == "V":
        return print('Siga')
    elif cor.upper() == "A":
        return print('Atenção')
    elif cor.upper() == "E":
        return print('Pare')

def main():

    cor = str(input())
    return sin(cor)

if __name__ == "__main__":
    main()
