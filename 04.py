def dig(num):
    if num >= 0 and num <= 9:
        return True
    else:
        return False

def main():
    num = float(input('escolha um número: '))
    print (f'{dig(num)}')

if __name__ == "__main__":
    main()
