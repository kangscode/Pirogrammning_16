import random

num = 0

def brGame(name):
    global num
    if name == "player":
        while(True):
            n = float(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if n != int(n):
                print("정수를 입력하세요")
            elif n<1 or n>3:
                print("1,2,3 중 하나를 입력하세요")
            else:
                n = int(n)
                for i in range(num, num+n):
                    print(name, ":", i+1)
                num += n
                break
        if num>=31:
            print("computer win!")
            exit(0)
    else:
        n = random.randint(1,3)
        for i in range(num, num+n):
            print(name, ":", i+1)
        num += n
        if num>=31:
            print("player win!")
            exit(0)

while True:
    brGame("computer")
    brGame("player")
   