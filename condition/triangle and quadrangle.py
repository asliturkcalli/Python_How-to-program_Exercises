print("if you want calculate triangle, enter 1 .","if you want calculate quadrangle,enter 2",sep="\n"*3 )
a=int(input("what is your decision"))

if a==1:
 x=int(input("enter first side"))
 y=int(input("enter second sides"))
 z=int(input("enter third sides"))
 if (abs(y-z)<x and x<y+z) and (abs(x-z)<y and y<x+z) and (abs(x-y)<z and z<x+y):
    if x==y==z:
      print("this is an equialateral triangle")
    elif (x==y and x!=z) or(x==z and x!=y)or (y==z and y!=x):
      print("this is ian isosceles triangle")
 else:
    print("this is not provides a condition being a triangle ")

elif a==2:
  first=int(input("enter first side"))
  second=int(input("enter second side"))
  third=int(input("enter third side"))
  fourth=int(input("enter fourth side"))
  if first==second==third==fourth:
    print("this is square")
  elif ((first==second)and(third==fourth))or((first==third)and(second==fourth))or((first==fourth)and(second==third)):
    print("this is rectangle")
  else:
    print("ordinary quadritaral")
else:
  print("pleas enter valid value")
