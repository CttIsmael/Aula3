def par(num):
    if (num % 2) == 0:
        return True
    else:
        return False

def main():
    num = int(input("digite um número: "))
    print(f'{par(num)}')


if __name__ == "__main__":
    main()
