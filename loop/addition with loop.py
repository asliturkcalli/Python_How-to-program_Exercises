"""*****addition with loop*****"""

print(""""if you want exit program ,enter q
      please enter number that you want to addition  """)
sum_varaible=0
while True:
    a=input("please enter a number")

    if a=="q":
        print(sum_varaible)
        break
    else:
        a=int(a)
        sum_varaible+=a



