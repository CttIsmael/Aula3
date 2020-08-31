def par(num):
    return not (num % 2 == 0)
    
def main():
    num = int(input())
    cod = par(num)
    print(cod)


if __name__ == "__main__":
    main()
