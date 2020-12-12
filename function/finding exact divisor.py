#exact divisor

def find_exact_divisor(number):
    exact_dvisor=[]
    for i in range(1,number+1):
        if number%i==0:
            exact_dvisor.append(i)

    return exact_dvisor


while True:
    number=input("enter a number=")

    if number=="q":
        break
    else:
        number=int(number)
        print(number,"exact divisor",find_exact_divisor(number))
