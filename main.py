print("welcome to the adventure park")
agree =str(input("would you like to try rollercoaster (y/n) "))
photo =str(input("do you want a photo? (y/n) "))
bill = 0
if agree == "y":
  height= int(input("enter your height please in cm "))
  age = int(input("enter your age please : "))
  if age >= 18 and age < 60:
      
      bill = 20
  elif age < 18 and age > 10:
    
    bill =10
  elif age < 10:
    print("you are under age")
  elif age >= 60:
      print("you must go to hospital grandpa")
  if photo == "y":
    bill +=3 
    print(f"your final bill {bill} $ , included a photo")
  else :
    print(f"your final bill {bill} , not icluded a photo")
  if height >= 120 and age < 60 and age > 10 :
    print("here are your tickets")
  else:
    print("sorry you can try other game")
  
  
else:
  other_game =str(input("what you would like to play  "))
  print(f"let's move to {other_game}")