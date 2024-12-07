playbutton=input(" Welcome to adventure game\n")
if playbutton == "play":
  loc1=input("you live in a little village but Recently Strangely,kids have been disappearing for exactly one hour, returning with their entire memory erased Choose where you want to go\n Cave Beach Desert\n")
  #cave entery
if loc1 == "cave":
  c1=input("you see a very cute little suspisious bunny in the cave do you pet it or run\n ")
  if c1=="pet it":
    print("it killed you")
   

  else:  
    print("you fell in a pit of gold but you die of stravation and lack of water")
   
   
   
if loc1=="beach":
  c2=input("There's a lot of things to do at the beach You can build a sand castle, dig a hole or swim\n")
  if c2 == "sand_castle":
    print("You build such a nice sandcastle, you decide to live in it. Then you get kidnapped and your memory gets erased.\n GAME OVER ")
  if  c2 == "swim":
    print("You accidently swim back to the village. But then you realize that the entire village has been kidnapped and returned without their memory. You were too late. GAME OVER")
  if c2 == "dig a hole":
    c3=input("While you were digging, you found a chest. Its unlocked. Do you open it?\n")
    if c3=="yes":
      c4=input("it has a paper inside which says:\n A solitary soul, a room confined,\n Sixty minutes, a test of mind. \nTrapped within, a silent plea,Who is the man who won't set me free. caleb jasper or abdul\n")
      if c4=="caleb":
        print("You captured and blamed the rong person. He sues you and you go to jail for life")
      if c4=="jasper":
        print("The judge thinks your crazy because a stone can't kidnap people. You are sent to jail for 1 hour.")
      if c4=="abdul":
        c5=input("Suddenly, he appears out of nowhere with an army of cute little sus bunnys. Do you run away or fight?\n")
        if c5=="run away":
          print("You escape but later your kidnapped. GAME OVER")
        if c5=="fight":
          print("You fought bravely and when you think all hope is gone, you find a can of bunny repellant in the chest and you use it to defeat the army of cute little sus bunnys. Then you capture abdul and give Everyone there memory back   you win\n")
         
       
     
    else:
      print("You decide not to open it and go back to the village. Then you change your mind and you go back to the beach. When you arrive, a cute little sus. bunny kills you. GAME OVER")
if loc1 == "desert":
  c6=input("you made it to the desert do you make a shelter or find water\n")
  if c6=="find water":
    print("you walk for about 3 hours then you die in a sand storm")
  if c6=="make a shelter":
    c7=input(" You accidentally find water while gathering materials to make your shelter Do you drink it?\n")
    if c7=="no":
      print(" You died You died of thirst")
    if c7=="yes":
      print(" Nearby, the water you found, There was a oasis You made your shelter and decided to live in it. You were never kidnapped But you never did solve the mystery. you lived happily ever after the end")
