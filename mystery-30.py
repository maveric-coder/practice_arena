while True:
    try:
        n=int(input())
        print(str(bin(n)).count('1'))
    except:
        break
