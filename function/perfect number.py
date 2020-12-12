
""" perfect number is a number whose sum of its exclusive divisors is equal to itself
forexample=6 exclusive divisors of 6=(1,2,3)
and sum of=1+2+3=6 """

def perfect_number(number):
    num=0
    for i in range(1,number):
        if number%i==0:
            num=num+i
        else:
            continue
    if num==number:
        return True
    else:
        return False

while True:
    number=input("enter a number")
    if number=="q":
        break
    else:
        number=int(number)
        if perfect_number(number):
            print(number,"is a perfect number")
        else:
            print(number,"is a not perfect number")

"""
def mukemmel(sayı):

    toplam = 0

    for i in range(1,sayı):

        if (sayı % i == 0):
            toplam += i

    return toplam == sayı


for i in range(1,1001):
    if (mukemmel(i)):
        print("Mükemmel Sayı:",i)

"""

