
def isprime(n):
    flg = 0
    for i in range(n):
        if(n % 2 == 0):
            print('Prime')
            flg = 1
            break
        else:
            continue
    if(flg == 0):
        print(n)


def main():
    for num in range(30,61):
        isprime(num)


if __name__ == "__main__":
    main()
