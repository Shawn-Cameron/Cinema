def individual():
  Tickets = 1
  age = int(input("How old are you"))
  if 0 < age <= 18:
    cost = 7
    print ("Your cost is $",cost,"have a nice day and enjoy the movie alone!")
    start_again = input("would you like to buy more tickets")
    if start_again == "y":
      start()
    else:
      print("Have a nice day and enjoy the movie")
  elif 18 < age <= 65:
    cost = 13
    print ("Your cost is $",cost)
    start_again = input("would you like to buy more tickets")
    if start_again == "y":
      start()
    else:
      print("Have a nice day and enjoy the movie")
  elif 110 > age >= 65:
    cost = 9
    print ("Your cost is $",cost,"have a nice day and enjoy the movie alone!")
    start_again = input("would you like to buy more tickets")
    if start_again == "y":
      start()
    else:
      print("Have a nice day and enjoy the movie")
  else:
    print ("Please restart and enter valid ages")
    start()
      
def group():
  x = -1
  Tickets = int(input("how many people are in your group"))
  total = 0
  for totalTickets in range(Tickets,x,-1):
    if totalTickets == 0:
      print("your total is $",total,"for",Tickets,"people,")
      print("Average cost per person is $",total/Tickets)
      start_again = input("would you like to buy more tickets")
      if start_again == "y":
        start()
      else:
        print("Have a nice day and enjoy the movie")
        break
    else:  
      age = int(input("How old are you"))
      if 0 < age <= 18:
        cost = 7
        total = total + cost
        print ("your curret cost is $",total)
      elif 19 <= age <= 65:
        cost = 13
        total = total + cost
        print ("your curret cost is $",total)
      elif 110 > age > 65:
        cost = 9
        total = total + cost
        print ("your curret cost is $",total)
      else:
        print ("Please restart and enter valid ages")
        start()
    
def start():
  start = input("Would you like to buy some tickets")
  if start == "y":
    people = input("Are you in a group(y/n)")
    if people == "y":
      group()
    elif people =="n":
      individual()
    
start()
  
