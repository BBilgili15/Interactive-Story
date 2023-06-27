import random, time, sys
from functions import *

#Title
input("The Saviours of Vulkanos - roll well to decide your fate")

# Players
player1 = Player(input("Enter Player 1 Name: "))
player2 = Player(input("Enter Player 2 Name: "))

# Variables
max_life = 100
dragons_chalice = False
gone_right = False


#Story

#Prologue
input("Prologue > ")
input("Through the billowing smoke, we decend on the murky town of Vulkanos - built into the side of a treacherous volcano. It’s home to only the toughest of the tough.")
input("The town thrives on its industry with some of the richest mining areas in all of the land.")
input("But don’t get the idea that these Vulkanites are wealthy. Oh no - evil lord Eruptus has been sucking the wealth out of Vulkanos for decades, leaving the people in poverty.")
input("His castle looms over the town, casting it in darkness. Any attempt to revolt has been met with an iron first – a trip to the gallows for any that dare to cross him.")
input("Stories tell of a prophecy that a dragon from the volcano will rise to liberate the people, although that belief has diminished with each generation that’s heard it.")
print("")

#Chapter 1

input("Chapter 1")
input(f"Meet our heroes, {player1.name} and {player2.name}. Sick and tired of the tyranny of Eruptus, they have decided to take on a mighty quest. To scale the mountain and find the dragon to save their town.")
input("In order to defend themselves from whatever may lie ahead, our heroes will need to find some weapons.")
input("Waiting until the dead of night, they creep out of their shack, making sure the coast is clear. At this time, the factories finally rest and the smoke has cleared from the sky. A full moon creeps out from behind the castle, its beams the most light Vulkanos ever sees.")
input(f"A miner by trade, {player1.name} leads them to the mineshaft. These tools could make perfect weapons for the journey.")
input(f"{player2.name} creaks open the door to the mine and our heroes enter. Once inside, they get to make their selection.")

print("""

Bow & Arrow (press “B”)
Crowbar (press “C”)
Dagger (press "D")
Hammer (press “H”)
Pick-Axe (press “P”)


""")


# Weapon Selection
player1.weapon_choice = (weapon_choice(player1))
player2.weapon_choice = (weapon_choice(player2))


#Chapter 2

input("Chapter 2")
input("With their new weapons in hand, our heroes look to exit Vulkanos and head for the summit of the volcano.")
input("If they leave the town to the left, they will have to cross a flowing river. If they leave the town to the right, they will have to cross land patrolled by Eruptus' guards")


# Decision Point 1 (Left or Right Route)
while True:
    decision1 = input("Which way should our heroes go? Left(L) or right(R)? ")

# Left Route
    if decision1.lower() == "l":
      input("They decide to head left to try to cross the river")
      input(f"They arrive at the river, flowing rapidly down the hill. {player2.name} finds a suitable crossing point although it doesn't look safe.")
      input("To cross safely, you each much roll a 4 or higher")

      # River Cross
      river_cross(player1)
      river_cross(player2)
      input("Our heroes drag themselves to the shore and dry off. The journey continues!")
      break

# Right Route
    elif decision1.lower() == "r":
        gone_right = True
        input(f"They continue carefully out of town and up the hill towards a nearby abandoned shack. {player2.name} suddenly holds out a hand.")
        input("One of Eruptus' patrol guards walks round from the shack and our heroes dive for cover behind a nearby bush.")
        input(f"{player1.name} and {player2.name} start to creep towards the back of the shack, in an attempt to sneak past. The guard is on high alert.")
        input("If you roll a 6, you will escape the guard's attention.")
        result = roll_dice()
        input("You rolled.......")
        input(result)
        if result > 5:
            input("Wow, what luck. Our heroes bypass the guard and march on!")
            break
        else:
            input(f"SNAP! {player1.name} steps on a branch and the guard rushes over!")
            input("He knows exactly who you are and draws his sword.")
            input("Roll your dice to attack the guard together! The higher the roll, the more damage you do!")

            # Fight the guard
            guard_battle(player1, player2)

            input(f"{player2.name} connects with their {player2.weapon['type']} and the guard falls to the ground, defeated!")
            input(f"The guard's sword slides along the grass to the feet of {player1.name} and {player2.name}.")
            input("The sword shines in the moonlight, its polished steel brighter than anything our heroes had seen in this wretched land.")
            while True:
                take_guard_sword = input(f"""Who will take the sword?

                {player1.name}: Enter "1"
                {player2.name}: Enter "2"
                Neither Player: Enter "3"

               ~ """)

                if take_guard_sword == "1":
                    player1.weapon["attack"] = 7
                    player1.weapon["range"] = 4
                    player1.weapon["type"] = "sword"
                    input(f"{player1.name} obtained the sword!")
                    break
                elif take_guard_sword == "2":
                    player2.weapon["attack"] = 7
                    player2.weapon["range"] = 4
                    player2.weapon["type"] = "sword"
                    input(f"{player2.name} obtained the sword!")
                    break
                elif take_guard_sword == "3":
                    print(f"{player2.name} tossed the sword into the bushes")
                    break
                else:
                    print("Please select from the options above...")

            input("Our heroes march on.....")
            break



# Terese Secret Unicorn Answer
    elif decision1.lower() == "unicorn":
        input(f"Suddenly through the trees, {player2.name} spots a magical unicorn. She approaches it with caution, holding out her hand as a sign of peace.")
        input("The unicorn nuzzles her hand and lets out a cry of 'AWOOOOOOO' to show love.")
        input(f"Together, {player2.name} and the unicorn save the town from Eruptus by shoving the unihorn up his asshole")
        break
    else:
        input("Please pick left or right")


print(f"""Health Update:

    {player1.name}'s health = {player1.life}/{max_life}
    {player2.name}'s health = {player2.life}/{max_life}

""")
input("")



# Chapter 3
input("Chapter 3")
input("Walking up through the boulders, our heroes continue onwards. They keep moving until a small cabin comes into sight, smoke pouring out of the chimney")
input("They approach the cabin and press an ear to the door. Psychotic laugher reverberates through the splintered, wooden exterior.")
input("Suddenly, the door BURSTS open, knocking them backwards!")
input("Witch: [CACKLE] Hello my travellers. Can I interest you in playing a little game with me? It could yield wonderful rewards")
input(f"{player1.name} and {player2.name} look at each other. They'll need all the help they can get to make it to the top of the volcano.")
input("They decide to play....")
input("Witch: The game is simple! All you have to do it guess the number I'm thinking of in 5 tries. It's between 1 and 50 and I'll even tell if you if you're too high or low...")
input("Witch: Sound too easy? Well what if I told you there was a punishment if you dont win? [CACKLE]")
input("Witch: First, you'll need to decide what you want to play for. Will it be for luck, for attack, or for health?")

witch_interaction(player1, player2)


print(f"""Health Update:

    {player1.name}'s health = {player1.life}/{max_life}
    {player2.name}'s health = {player2.life}/{max_life}

""")
input("")


#Chapter 4

input("Chapter 4")
input("For hours they continue on upwards through the rocky wasteland. The barren landscape slowly starts to gives way with shrubbery and trees sprouting by the mile.")
input("With aching limbs and bloody boots, they stumble upon a river by a wooded area. The perfect spot to set up camp.")
input("After scanning the area, our heroes realise they have two options if they want to eat tonight.")
input("One of them can climb a nearby coconut tree or they can both attempt to hunt a wild boar. The tree climb will be easier but the boar will make a great meal, if caught.")

# Decision Point 2 - Tree Climb / Boar Hunt:

while True:
    decision = input("""

    Climb the coconut tree ("C")

    Hunt a wild boar ("H")


~ """)

    # Tree Climb Route

#The lucky dice impacts coconut climb (lucky dice makes it harder – unlucky dice makes it easier). Am I ok with that?

    if decision.lower() == "c":
        input("The tree looks to be the best option. Boars are wiley and notoriously difficult to hunt.")
        input("Roll anything but a 6 to keep climbing. If you roll a 6, prepare to fall to the ground below..")
        while True:
            climber = input(f"""Who will volunteer to climb the tree?

        {player1.name} ("1")
        {player2.name} ("2")

           ~ """)

            if climber == "1":
                tree_climb(player1, player2)
                break

            elif climber == "2":
                tree_climb(player2, player1)
                break

            else:
                input("Please select 1 or 2..")

        break


    # Boar Hunt Route
    elif decision.lower() == "h":
        input("The boar looks to be the best option. The tree is tall and looks difficult to scale.")
        input("Our heroes creep into the woodland silently, ears pealed for any sounds.")
        input("There! A small boar wanders into view, unaware of their presence.")
        result = boar_hunt()
        if result == "fail":
            # Add a bit more narrative before spotting each boar
            input("You spot a second boar")
            result = boar_hunt()
            if result == "fail":
                input("You spot a third boar")
                result = boar_hunt()
                if result == "fail":
                    input("Three chances failed... Our heroes will go hungry tonight...")
                    input("All that wasted energy.. 10 health points lost from each player")
                    Player.alter_health(player1, -10)
                    Player.alter_health(player2, -10)
                    break
                else:
                    input("Our heroes eat well tonight. 10 health points recovered!")
                    Player.alter_health(player1, 10)
                    Player.alter_health(player2, 10)
                    break
            else:
                input("Our heroes eat well tonight. 20 health points recovered!")
                Player.alter_health(player1, 20)
                Player.alter_health(player1, 20)
                break

        else:
            input("Our heroes eat well tonight. 30 health points recovered!")
            Player.alter_health(player1, 30)
            Player.alter_health(player2, 30)
            break


    else:
        input("Please enter Climb ('C') or Hunt ('H')")


# Health Update
input(f"""

        {player1.name}'s health = {player1.life}/{max_life}
        {player2.name}'s health = {player2.life}/{max_life}

    """)


input("Chapter 5")
input("Our heroes awaken to the sound of birdsong. Still half asleep, they have no idea where they are – the woodland paradise feels like a dream.")
input("Suddenly, the illusion wears off and the pains and aches of sleeping on the forest floor all return at once. It’s time to move.")
input("Packing up their things, our heroes continue onwards. As long as they’re walking uphill, they’re going the right way.")
input(f"After a short walk, they stumble across a sheer cliff-face. Moss has claimed most of its surface and vines reach down towards them from the summit. {player2.name} spots a shadow further along.")
input("Upon investigation, the shadow is actually the entrance to a cave. They wander inside to check it out.")
input("Cracks in the rock allow beams of light to pour in and guide them forward. The light illuminates etchings on the wall, worn down over time. The players can make out a figure of a dragon, fire erupting from its mouth, with bodies strewn on the ground around it. A golden chalice has been carved above the sketch. What could it mean?")
input("Below the drawings sits an ancient looking chest, half buried by the sandy floor over time. Digging it out, it’s clear that a crowbar might be able to prise it open.")

if player1.weapon['type'] == "crowbar":
    open_chest(player1)
    dragons_chalice = True

elif player2.weapon['type'] == "crowbar":
    open_chest(player2)
    dragons_chalice = True

else:
    input("If only one of them had picked up a crowbar from the mineshaft....")
    input(f"{player1.name} whacks the chest with their {player1.weapon['type']}, but it doesn't budge. There's no chance of getting it open...")

input("Further into the cave, they start to climb upwards. Steps cut into the rock have clearly been made by humans. Who used to live here? Whoever it was, they’ve made life easier for our heroes as they continue to climb.")
input("Hundreds of steps later with burning thighs, the sky comes back into sight at last.")
input(f"{player2.name} reaches for a wooden handle, perfectly positioned to pull themselves up. It gives way and slides down with a metallic clunk…. That didn’t sound good.")
input("A rumble begins. Initially far away but growing louder and louder by the second. The floor starts to shake and grit rains down from above. Could it be? That the cave was booby trapped?")
input("Our heroes start to the rush to the summit as the cave begins to collapse in on itself.")

rock_dodge(player1, -10)
rock_dodge(player2, -25)
rock_dodge(player1, -50)

input("Our heroes, scramble to the summit and hoist themselves up, into the open air just as the last steps fall away beneath them. That was close. After a few seconds, the last of the rocks crash against the cave floor, hundreds of meters below and there is silence. They take a second to catch their breath.")
input("[ROOOOAAAAARRRRRRR]")
input("What was that? A chilling roar, louder than any factory in Vulkanos, splits the sky. Could it be the dragon that they’re looking for?")
input("The summit of the volcano is looking closer than ever. The air is thick with smoke and the smell of sulphur burns in the nose. Not far to go.")

input(f"""

        {player1.name}'s health = {player1.life}/{max_life}
        {player2.name}'s health = {player2.life}/{max_life}

    """)



# Chapter 6

input("Chapter 6")
input(f"With the narrow escape behind them {player1.name} and {player2.name} trudge on.")
input(f"After a while, {player1.name} signals to stop. Is that the sound of voices?")
input("[SPREAD OUT AND SEARCH! BRING THEM BACK DEAD OR ALIVE!]")
if gone_right == True:
    input("It must be more of Eruptus’ guards and, by the sound of it, a squadron leader as well. They must have found of the body of the guard killed earlier and sent reinforcements.")
else:
    input("It must be more of Eruptus’ guards and, by the sound of it, a squadron leader as well. The guards never come this far up the volcano. They must know exactly what are heroes are up to.")
input("Creeping forward under the cover of the rocks, three guards and their leader come into sight.")
input(f"The guards are tough, but being able to raid the supplies of a group will be invaluable…. {player1.name} and {player2.name} decide to take them on!")
input("They leap over the rocks towards the guards who immediately spin round, weapons raised!")


multiple_guard_battle(player1, player2)

input("Success! Eruptus' guards lay slain on the floor")





# Make the original guard fight like this

# Make new weapon selection
# FLAIL, LONGSWORD, CROSSBOW, MACE