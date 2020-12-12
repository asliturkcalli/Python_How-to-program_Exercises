"""***** even number calculator*****"""


a=int(input("please enter range"))
even_num_set=[]
for i in range(a):
    if i%2==0:
        even_num_set.append(i)
    else:
       continue

print(even_num_set)
        
