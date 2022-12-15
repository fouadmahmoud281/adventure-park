print("welcome to the adventure park")
agree =str(input("would you like to try rollercoaster (y/n) "))
if agree == "y":
  height= int(input("enter your height please in cm "))
  age = int(input("enter your age please : "))
  if age >= 18 :
      print("your tickets will cost 20$")
  else:
      print("your ticket will cost 10$")
  if height >= 120 :
    print("here are your tickets")
  else:
    print("sorry you can try other game")
  
else:
  other_game =str(input("what you would like to play  "))
  print(f"let's move to {other_game}")