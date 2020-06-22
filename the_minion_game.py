def minion_game(string):
   
    s=string
    vowels='AIEOU'
    kev=0
    stu=0
    for i in range(len(s)):
        if s[i] in vowels:
            kev+=len(s)-i
        else:
            stu+=len(s)-i
    if kev>stu:
        print("Kevin",kev)
    elif stu>kev:
        print("Stuart",stu)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
