print("*****prime finding*****")
#prime number is a number that cannot be divided by a numbe except itself and 1

def prime_number(number):
    if (number==1):
        return False
    elif(number==2):
        return True
    else:
        for i in range(2,number):
            if (number%i==0):
                return False
            else:
                return True
while True:
    number=input("enter a number=")

    if number=="q":
        print("exiting program")
        break
    else:
        number=int(number)
        if prime_number(number):
            print(number," prime number")
        else:
            print(number,"is not prime number")

