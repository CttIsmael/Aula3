def nota(n1, n2, n3):
    media = (n1 + n2 + n3)//3
    if n3 > 8:
        media = ((n1 + n2 + n3)//3) + 1

    else:
        media = (n1+n2+n3)/3

    if media > 10:
        return 10

    return print(f'{media}')

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    return nota(n1, n2, n3)

if __name__ == "__main__":
    main()
