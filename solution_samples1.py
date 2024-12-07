import random
#for random codes
Go=0
#Go means game over?
treasure = {"something", "Anotherthing"}
"Treasure"
location ={
  "Forest" : "bear",
  "Beach" : "shovel",
  "Mountain" : "coins",
  "River" : "spaceship",
  "Cave" : "empty"
}
print("***\tWelcome to the Adventure Game!\t***\n Your name is Martin Notchess\n Here, you will explore regions to find treasure\n(Background music playing)")
while True:
  cn = input("Would you like to continue?(yes or no)")
  if cn== "no":
    break
  #cn means continue?
  region = input("Choose which location to go: \n\tForest\n\tBeach\n\tMountain\n\tRiver\n\tCave\n")
  if region == "Forest":
    import random
    random = random.randint(1,3)
    if random == 1:
      print("You found wood!")
      treasure.add("wood")
    else:
      print("You found a wild bear")
      bc = input("Would you like to fight or run")
      #bc means bear choice
      if bc == "run":
        continue
      else:
        if "sword" in treasure:
          print("Congratulations! You took out your sword and killed the bear with handle! You found meat!")
          treasure.add("meat")
        else:
          print("Game over, you died")
          Go = 1
          break
  if region == "Beach":
    print("You found a shovel!")
    treasure.add("shovel")
    dc=input("You found an X on the floor. Do you want to dig it up? (yes or no)")
    #dc means dig choice
    if dc == "yes":
      print("You start digging when a bunch of pirates surprise you and kill you!\n Game over, you die.")
      Go=1
      break
      Go=1
    else:
      print("You leave the X alone")
      continue
  if region=="Mountain":
    print("You found coins, they're incredibly mushy\nYou see a yak.")
    yc = input("You can hit it or you can feed it your coins(yak may choke)")
    #yc means yak choice
    if yc=="hit":
      print("You find yourself dead by an angry yak.\nGame over, you die.")
      Go=1
      break
    else:
      print("The coins are chocolat! The yak loves chocolat. The yak gives you its horns and you make a sword! (somehow).")
      treasure.add("sword")
      continue
  if region=="River":
    print("You find a spaceship!")
    sc = input("Would you like to fly to space, yes or no?(you may not return)")
    #sc means space choice
    if sc == "yes":
      print("You enter the shuttle and wait for the countdown\n3...\n2...\n1...\nBlast off! You soar into space and realize you have no idea what you are doing.\nYou find yourself being attacked by Emperror WizYoFu from an alien planet.\nGame over, you die.")
      Go=1
      #Go means game over?
      break
    else:
      print("You realize you have no idea how to control a spaceship so you leave")
      continue
  if region =="Cave":
    print("You enter the cave")
    if "wood"in treasure:
      Yeti=input("You make a fire with your wood and you see an abominable snowman(ominous music) do you want to fight or run")
      treasure.remove("wood")
      if Yeti == "fight":
       print("Congratulations! You beat the abominable snowman with the burning plank while accidently burning your hair off! You got the treasure of baldness!")
       treasure.add("Bald")
       continue
      else:
        print("You leave")
        continue
    else:
      print("You can not see anything, you leave")
      continue
treasure.remove("something")
treasure.remove("Anotherthing")
if Go == 1:
  print("Nice try")
else:
  print("Good Job! You win! These are your treasures:")
  for d in treasure:
    print(d)
