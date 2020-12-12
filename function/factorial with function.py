def factorial(num):
    factorial=1
    if num==0 or num==1:
        return 1
    else:
        """while(num>1):
          factorial=factorial*num
          num=num-1
        return factorial"""
        for i in range(1,num+1):
           factorial*=i
        return factorial

num=int(input("enter a number"))
print(factorial(num))
