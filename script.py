import random
num = random.randint(0, 100)
n=int(input())
while True:
    if(n>num):
        print("Less")
    elif(n<num):
        print("More")
    else:
        print("Bingo!")
        break
    n=int(input())
