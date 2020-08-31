def nota(n1, n2, n3):
    media = (n1 + n2 + n3)//3
    if n3 > 8:
        media + 1
    elif media > 10:
        media = 10
    return print (f'{media}')

def main():
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    n3 = int(input('Nota 3: '))
    return nota(n1, n2, n3)

if __name__ == "__main__":
    main()
