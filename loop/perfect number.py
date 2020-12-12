""" perfect number is a number whose sum of its exclusive divisors is equal to itself
forexample=6 exclusive divisors of 6=(1,2,3)
and sum of=1+2+3=6 """

while True:
    num=int(input("enter a number"))
    result=0

    for i in range(1,num):
        if num%i==0:
            result=result+i
        else:
            continue

    if result==num:
                print("perfect number")
    else:
                print("not perfect number")
    if num==0:
          print("exiting program")
          break
