import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
gold coins = 0

required = ("\nUse only A, B, or C\n") 

#The story is broken into sections, starting with "intro"
def intro():
  print ("you were going on a long trip and you got a nap , you awaken the "
  "next morning in a thick, dark island.  " 
  " you stand and observe at your new, "
  "unfamiliar place. The silence quickly fades when you hear a "
  "shouting sound coming behind you. A group of robbers is "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the robbers.
  B. stand their and wait for the robbers
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, you are so lazy. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nsome of the robbers gets stunned, but regains control. they begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "robers head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "dread. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "roberrs have dog they can easily find you, right? Not sure, but "
    "for me it is YES, so...\n\nYou died!")
  elif choice in answer_B:
   if spear > 0:
    print ("\nYou laid in wait. The shining sword attracted "
    "the roberrs, which thought you were no match. As he walked "
    "closer and closer, your heart beat increases rapidly. As the roberrs  "
    "reached out to grab the sword, you pierced the blade into "
    "their chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the robbers enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the robbers turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the robbers "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind bushes
  B. Trapped, so you fight
  C. Run towards an abandoned village""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an robbers. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_village()
  else:
    print (required)
    option_run()
    
def option_village():
  print ("\nWhile drastically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a broken building, waiting for the robbers to come "
  "charging around the corner. You notice gold coins  "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    gold coins = 1 #adds a gold coins
  else:
    gold coins = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending gold coins.")
  time.sleep(1)
  if gold coins > 0:
    print ("\nYou quickly hold out the golden coins, somehow "
    "hoping it will stop the robbers. It does! The robbers was looking "
    "for gold coins. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the gold coins. "
     "\n\nYou died!")

intro()