#Write a program that produce the following output giving an integer input n.
#3.1
def star3_1(number):
    print("n=",number)
    for i in range(1,number+1):
        for j in range(i):
            print("*", end="")
        print("")

#3.2
def star3_2(number):
    print("n=",number)
    for i in range(1,number+1):
        for j in range(i,number):
            print(" ", end="")
        for k in range(i):
            print("*", end="")            
        print("")

#3.3
def star3_3(number):
    print("n=",number)
    for i in range(1,number+1):
        for j in range(i,number):
            print(" ", end="")
        for j in range((i*2)-1):
            if j==0 or j==(i*2)-2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

#3.4
def star3_4(number):
    print("n=",number)
    for i in range(0,number):
        for j in range(0,number):
            if j==i or j==number-i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

#3.5
def star3_5(number):
    print("n=",number)
    for i in range(number+1):
        if i%2 != 0:
            a = (number - i) // 2
            print (" "*a + "*"*(i) + " "*a)
    for j in range(number-1,0,-1):
        if j%2 != 0:
            b = (number-j)//2
            print (" "*b + "*"*(j) + " "*b)

#3.6
def star3_6(number):
    print("n=",number)
    for i in range(1,number+1):
        for f in range(number-i):
            print('A', end="")
        for j in range((i*2)-1):
            if j==0 or j==(i*2)-2:
                print("+", end="")
            else:
                print("E", end="")
        for f in range(number-i):
            print('B', end="")
        print("")
    for i in range(1,number):
        for f in range(i):
            print("C",end="")
        for j in range((number*2)-(i*2)-1):
            if j==0 or j==range((number*2)-(i*2)-1)[-1]:
                print("+", end="")
            else:
                print("E", end="")
        for f in range(i):
            print("D",end="")
        print("")

# 4
# (Python specific) In Python, what is the difference between else and finally in exception handling?
# Answer 'else' will execute when there is no exception from condition which unlike 'finally' that always execute even there is exception or not.

n = int(input("Enter number to process : "))
star3_1(n)
star3_2(n)
star3_3(n)
star3_4(n)
star3_5(n)
star3_6(n)