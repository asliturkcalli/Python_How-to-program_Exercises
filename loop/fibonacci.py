print("***********",
       "fibonacci",
       "***********",sep="\n")

a=1
b=1
range_user=int(input("enter a range"))
fibonacci=[a,b]
for i in range(range_user):
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)
