# sdf
def city_status():
  print("What city do you want to explore?")
  for i in range(len(city_dict)):
    print(f"{i+1}. {list(city_dict.keys())[i]}")
#ghskfjsfisnj
  location = int(input("Enter(1-7): "))
  print()
  
  if ((location > len(city_dict)) or (location < 0)):
    print("Invalid input")

  else:
    location = list(city_dict.keys())[location-1]
    
    min_hour_per_week = city_dict[location][0]/(4*city_dict[location][1])
    print(f"Average living cost in {location} is ${city_dict[location][0]}")
    print(f"Minimum living wage in {location} is ${city_dict[location][1]}")
    print(f"Minimum hours you need to work to meet the minimum living cost is {min_hour_per_week:.2f} hours per week.")
    print()
  


city_dict = {
  "Chicago": [1267.3, 15],
  "New York": [2500, 16],
  "Seattle":  [1427.6, 17.25],
  "Los Angeles": [1363.1,16.00],
  "San Francisco": [1489.4,16.00],
  "Miami": [1295.6,13],
  "San Antonio": [1113.9,7.25]
}

# option for age below 10
age_below_10 = {
  "Snacks": [["M&M's", 2.00], ["Skittles", 2.00], ["Reese's", 2.00]],
  "Drinks": [["Choclate Milk", 3.00], ["Strawberry Milk", 3.00], ["CapriSun", 4.00]],
  "Games": [["Snake & Ladder", 6.00], ["Pokemon Cards", 5.00], ["Small Stuffed animal", 8.00]]
}
# option for age below 15
age_below_15 = {
  "Snacks" : [["Fries", 5.00], ["Popcorn", 7.00], ["Chips", 4.00], ["Ice Cream", 5.00]],
  "Drinks" : [["Coke", 2.00], ["Sprite", 2.00], ["Lemonade", 2.00], ["Smoothie", 3.00]],
  "Games" : [["UNO", 5.00], ["Pokemon Card", 5.00], ["Catan", 12.00], ["Frisbee", 7.00]]
}
# option for age below 21
age_below_21 = {
  "Snacks": [["Chips", 7.00], ["Popcorn", 10.00], ["Ramen", 20.00], ["Pasta", 20.00]],
  "Drinks": [["Coke", 10.00], ["Sprite", 10.00], ["Boba", 10.00], ["Smoothie", 15.00]],
  "Games": [["UNO", 7.00], ["Minecraft", 20.00], ["XBox Game Pass", 20.00], ["Cards", 20.00]]
}
# option for age 21 and above
age_21_and_above = {
  "Snacks" : [["Chips", 7.00], ["Popcorn", 10.00], ["Ramen", 20.00], ["Pasta", 20.00], ["Meal Outside", 20.00]],
  "Drinks" : [["Coke", 10.00], ["Sprite", 10.00], ["Boba", 10.00], ["Smoothie", 15.00],["Alcohol", 20.00]],
  "Games" : [["UNO", 7.00], ["Minecraft", 20.00], ["XBox Game Pass", 20.00], ["Cards", 20.00],["Genshin 10 pulls", 20.00]]
}

print("Hi, Welcome to our game!\n") # add game name later

# menu option
# print("Here's the Menu:")
# print("1. City Stats")
# print("2. Shopping Game")
# print("3. Exit")
# print()

option = 0;
while (option != 3):
  print("Here's the Menu:")
  print("1. City Stats")
  print("2. Shopping Game")
  print("3. Exit")
  print()
  option = int(input("Enter your option: "))
  if (option ==3):
    break
  if (option == 1):
    intent_continue = True
    while(intent_continue):
      city_status()
      user_intent = input("Try another city?(y/n): ")
      print()
      if (user_intent == "n"):
        intent_continue = False
  
  # game
  elif (option == 2):
    continue_game = "y"
    while (continue_game == "y"):
    
      print("Let's play a financial game....")
      
      age = int(input("\nEnter your age: "))
    
      if ((age <= 10)):
        allowance = 10
        item_dict = age_below_10
    
      elif (age <= 15):
        allowance = 20
        item_dict = age_below_15
    
      elif (age < 21):
        allowance = 30
        item_dict = age_below_21
    
      else:
        allowance = 40
        item_dict = age_21_and_above
      
      print("\nYou will be given $" +str(allowance)+". Budget and spend your money wisely.\n")
    
      print("These are your options:\n")
      for i in range(len(list(item_dict.keys()))):
        print(f"{list(item_dict.keys())[i]}")
        for j in range(len(item_dict[list(item_dict.keys())[i]])):
          print(f"{i+1}.{j+1}. {item_dict[list(item_dict.keys())[i]][j][0]:15}", end=": ")
          print(f"${item_dict[list(item_dict.keys())[i]][j][1]:6.2f}")
        print()
    
      quantity = int(input("\nHow many items do you want to buy? "))
      total = 0
      for i in range(quantity):
        item = input("\nEnter the item number you want to buy: ")
        price = item_dict[list(item_dict.keys())[(int(item[0]))-1]][(int(item[2]))-1][1]
        total += price
      user_total = int(input("\nGuess the total: "))
      if (user_total == total):
        print("\nYou are correct! The Price is $" + str(total))
      else:
        print("\nYou are wrong. The Price is $" + str(total))
      budget = input("\nIs the total within the budget(y/n): ")
      if (total <= allowance):
        if(budget == "y"):
          print("\nYou are correct! You can buy these items!")
        else:
          print("\nYou are wrong. You can buy these items.")
      else:
        if(budget == "n"):
          print("\nYou are correct! You can't buy these items.")

        else:
          print("\nYou are wrong. You can't buy these items.")
      

      continue_game = input("\nDo you want to continue playing game?(y/n): ")
  else:
    print("Invalid input")
    print()
    continue
  
  continue_option = input("\nDo you want to explore other function?(y/n): ")
  print()
  if continue_option == "n":
    break
  
# exiting the program
print("\nThank you for using our program!")
