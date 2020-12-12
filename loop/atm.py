print("transaction:",
      "1.blance inquiry=1",
      "2.withdraw money=2",
      "3.deposit money=3",
      "Enter the number of the transaction you want",
      "press q to exit",sep="\n")
blance=(input("how much is your current blance"))
while True:

 x=input("what is your transaction you want to do")


 if x=="q":
     print("exiting the program")
     break
 elif x=="1":
     print("your blance{}".format(blance))
 elif x=="2":
     blance=int(blance)
     amount=int(input("enter amount you want"))
     if amount>blance:
         print("unsufficient fund")
         continue
     else:
         blance-=amount
         print("your blance{} ".format(blance))
 elif x=="3":
     blance=int(blance)
     amount=(int(input("enter amount you want")))
     blance+=amount
     print("your blance{}".format(blance))
 else:
     print("please enter valid value")

