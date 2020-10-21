def hack(number,fac1,fac2):

    number1 = number
    number2 = number
    number1 /= fac1
    number2 /= fac2
    if number1 == 1 or number2 == 1:
        return True

    elif number1 < 1 or number2 < 1:
        return False

    if hack(number1,10,20) or hack(number2,10,20):
        return True

for  _ in range(int(input())):
    n=int(input())
    if n == 1:
        print("Yes")
        continue

    if hack(n,10,20):
        print("Yes")
    else:
        print("No")
