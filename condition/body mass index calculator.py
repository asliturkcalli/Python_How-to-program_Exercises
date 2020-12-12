print("**********","body mass index","**********",sep="\n")

weight=float(input("enter your weight"))
height=float(input("enter your height"))

body_mass_index=weight/(height*height)

if body_mass_index < 18.5:
  print(f"your body mas index={body_mass_index} and you are slim")
elif body_mass_index>=18.5 and body_mass_index<25:
  print(f"your body mas index={body_mass_index}and you are normal")
elif body_mass_index>=25 and body_mass_index<30:
  print(f"your body mass index={body_mass_index}and you are over weight" )
elif body_mass_index>=30:
  print(f"your body mas index ={body_mass_index}and you are obez")
else:
  print("please you enter valid value")
