# Title
print("                   ~ American Racer ~")
print()

#Introduction
print("The Story of an espiring Race car driver")
print()
print("Your an amatuer driver in the race car circuit and you want to be a professional driver on day." )
print()
print("You've just won your first amature race!")

#Multiple Choice option
print()
print("There are three man waiting to talk to you outside the stadium: ")
print("a. A sponsor, who needs someone to race for his brand.")
print("b. A trainer would like to teach him how to become a professional driver. ")
print("c. A local street racer that wants to have a conversation with you.")
print("d. A guy in a black jacket with a trench coat was waiting to talk to you.")
myoption = input("Enter who you like to speak with: ")
print()

#If Statement in yes or no results.
if(myoption == "a"):
  print("You have to pass your training to become a professional driver")
  myoption = input("Would you like to  proceed yes or no: ")
  if(myoption == "yes"):
    print("You've just completed your training and to your first professional race. Congratulations to your new career!!! ")
  elif(myoption == "no"):
     print("You will go back to the race car circuit. ")

# Solving a problem in a riddle.
math = input("I need to test out your math skills kid! If I have five cars in the parking lot and I removed three how many cars do I currently have in the parking lot? ")

if(math == "b"):
  
  print("I need to test out your math skills kid! If I have five cars in the parking lot and I removed three how many cars do I currently have in the parking lot? ")
  

if(math == "2"):
  print("Instead of racing cars i think you would be a better accountant for my company! And american race became a sucessful accountant instead of pursuing his dreams. ")
else:
    print("I cant use you kid! Gameover")

#Solving a problem in yes or no
question = input ("Can I show you my racing skills? Yes or No: ")

if(question == "c"):
  if(question == "yes"):
    print("You both get into a car wreck which ends your career. Gameover! ")

if(question == "no"):
  print("You go home and get to race another day")

#Giving a yes or no response with myoption D
if(myoption == "d"):
  print("The guy in the trench coat offered you a thousand dollars to drive him across state lines. ")
  
  driver = input("Do you accept the offer yes or no: ")

if(driver == "yes"):
  print("You go on a high speed chase with polic and get caught. Gameover! ")

if(driver == "no"):
  print("You go home and continue as a circuit racer.")
  



  
  




