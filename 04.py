def dig(num):
    if num in '0 1 2 3 4 5 6 7 8 9':
        return True
    else:
        return False

def main():
    num = str(input())
    print (f'{dig(num)}')

if __name__ == "__main__":
    main()

