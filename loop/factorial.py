print("*************************",
      "factorial finder program",
      "press q to exit",
      "*************************",sep="\n")
while True:
    num=input("enter the number whose factorial you want to find")
    if num=="q" or num=="Q":
        print("exiting the program")
        break
    else:
       num=int(num)
       factorial=1

