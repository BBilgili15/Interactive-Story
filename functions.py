import random, sys, time

# Classes
class Player:

    def __init__(self, name):
        self.name = name
        self.life = 100
        # self.weapon = Weapon
        self.weapon = {
            "type": "",
            "attack": 0,       # Out of 10
            "range": 0         # Out of 10
        }

    # is sys.exit ok to use?
    def alter_health(player, change):
        max_life = 100
        if (player.life + change) > max_life:
            player.life = 100
        else:
            player.life += change
            if player.life <= 0:
                print(f"{player.name} died.... Game Over!")
                return sys.exit()
            else:
                return player.life


# Need to find more uses for enemies
# class Enemy:

#     def __init__(self, name, life):
#         self.name = name
#         self.life = life

class Guard:

    def __init__(self, name):
        self.name = name
        self.life = 15
        self.attack = -15

    def random_attack_player(player1, player2):
        selection = random.randint(1, 2)
        if selection == 1:
            target = player1
        else:
            target = player2
        Player.alter_health(target, -15)
        return target

class Guard_leader:

    def __init__(self):
        self.name = "Guard Leader"
        self.life = 30
        self.attack = -25

    def random_attack_player(player1, player2):
        selection = random.randint(1, 2)
        if selection == 1:
            target = player1
        else:
            target = player2
        Player.alter_health(target, -25)
        return target


# Unsure on how to actually run with weapons as classes
class Weapon:

    def __init__(self, name, attack, range):
        self.name = name
        self.attack = attack
        self.range = range

# Functions
dice_range = 1

# Roll Dice
def roll_dice():
  result = random.randint(dice_range, 6)
  return result

# Standard Dice (doesn't change with witch encounter) def roll_standard_dice():
def roll_standard_dice():
  result = random.randint(1, 6)
  return result

# Multiple Dice
def roll_multiple_dice(num_dice=1):
  result = 0
  dice_num = 1
  while num_dice >= 1:
    roll = random.randint(dice_range, 6)
    input("")
    print(f"Dice {dice_num}: {roll}")
    result += roll
    dice_num += 1
    num_dice -= 1
  return result


# Initial Weapon Choice
def weapon_choice(player):
    while True:
        selection = input(f"{player.name}, what will you choose? ")
        if selection.upper() == "B":
            player.weapon["attack"] = 4
            player.weapon["range"] = 8
            player.weapon["type"] = "bow & arrow"

            break

        elif selection.upper() == "D":
            player.weapon["attack"] = 5
            player.weapon["range"] = 2
            player.weapon["type"] = "dagger"
            break

        elif selection.upper() == "C":
            player.weapon["attack"] = 1
            player.weapon["range"] = 2
            player.weapon["type"] = "crowbar"
            break

        elif selection.upper() == "H":
            player.weapon["attack"] = 4
            player.weapon["range"] = 2
            player.weapon["type"] = "hammer"
            break

        elif selection.upper() == "P":
            player.weapon["attack"] = 6
            player.weapon["range"] = 4
            player.weapon["type"] = "pickaxe"
            break

        else:
            print("Please pick from the above options")

    input(f"{player.name} acquired the {player.weapon['type']}!")
    return player


# River Cross
def river_cross(player):
    input(f"{player.name} tries to cross...")
    player_cross_count = 0
    while player_cross_count < 3:
        result = roll_dice()
        input("You rolled.......")
        input(result)
        if result > 3:
          input(f"{player.name} crossed successfully!")
          break
        else:
          Player.alter_health(player, -10)
          input(f"{player.name} got caught up in the current and lost 10 health. Current health now {player.life}!")
          player_cross_count += 1


# Guard Battle
# Changed health to 14 and damage to 15 as a trial def guard_battle(player1, player2):
def guard_battle(player1, player2):
    guard_life = 14
    while guard_life > 0:
        result = roll_dice()
        input("You rolled.......")
        input(result)
        guard_life = (guard_life - result - player1.weapon['attack'] - player2.weapon['attack'])
        if guard_life > 0:
            Player.alter_health(player1, -15)
            Player.alter_health(player2, -15)
            input("The guard survives your attack and catches you with his sword. 15 points are lost from the health of our heroes!")
            input("You attack again!")

# Wicked Witch Game
# If you hit enter or type a letter, it breaks. Need a Try function here to catch the error?
def guess_the_number():
    witch_number = random.randint(1, 50)
    guess_count = 1
    while guess_count < 6:
        try:
            guess = int(input(f"Guess {guess_count}: "))
            if guess > witch_number:
                if guess > 50:
                    print("You may only guess from 1 to 50...")
                else:
                    print("NOPE, too high")
                    guess_count += 1
            elif guess < witch_number:
                if guess < 1:
                    print("You may only guess from 1 to 50...")
                else:
                    print("NOPE, too low")
                    guess_count += 1
            else:
                input("WHAT, YOU GOT IT RIGHT?????")
                return "success"
        except (SyntaxError, ValueError):
            print("You may only guess numbers, my travellers...")
    input(f"So close yet so far. The number I was thinking of was {witch_number}...")
    return "fail"

# Wicked Witch Interaction
def witch_interaction(player1, player2):
    while True:
        choice = input("""So what will you choose?

        Luck ('L')
        Attack ('A')
        Health ('H')

~ """)
        if choice.lower() == "l":
            input("Witch: [CACKLE] Ahh you chose LUCK!")
            input("If you win, I'll stop you from rolling a 1 for the rest of your journey....")
            input("buuuut.......")
            input("If you lose, I'll add a 0 to your dice!")
            input("Let's begin.....")
            result = guess_the_number()
            global dice_range
            if result == "success":
                input("[sigh] As promised, here you go.. The 1 has vanished from your dice...")
                input("Now get out of here before you see my nasty side..")
                dice_range = 2
                break
            else:
                input("[CACKLE] As promised, a 0 has been added to your dice! Good luck my travellers.... You'll need it.....")
                dice_range = 0
                break

        elif choice.lower() == "h":
            input("Witch: [CACKLE] Ahh you chose HEALTH!")
            input("If you win, I'll heal you fully....")
            input("buuuut.......")
            input("If you lose, I'll reduce your health by half!")
            input("Let's begin.....")
            result = guess_the_number()
            if result == "success":
                input("[sigh] As promised, here you go.... You are both at max health...")
                input("Now get out of here before you see my nasty side..")
                player1.life = 100
                player2.life = 100
                break
            else:
                input("[CACKLE] As promised, both your health points have been HALVED!")
                player1.life /= 2
                player2.life /= 2
                break


        elif choice.lower() == "a":
            input("Witch: [CACKLE] Ahh you chose ATTACK!")
            input("If you win, I'll increase the attack stat of your weapons....")
            input("buuuut.......")
            input("If you lose, I'll reduce the attack stat by the same amount!")
            input("Let's begin.....")
            result = guess_the_number()
            if result == "success":
                input("[sigh] As promised, here you go.. Your weapons' attack have been increased by 2. Happy hunting...")
                input("Now get out of here before you see my nasty side..")
                player1.weapon['attack'] += 2
                player2.weapon['attack'] += 2
                break
            else:
                input("[CACKLE] As promised, your weapons' attack have been reduced by 1. Happy hunting...")
                player1.weapon['attack'] -= 2
                player2.weapon['attack'] -= 2
                break

        else:
            print("Please pick Luck ('L'), Attack ('A') or Health ('H')...")


# Tree Climb
def tree_climb(climber, other):
    count = 0
    height = 1
    while count < 3:
        input(f"{climber.name} climbs..")
        result = roll_dice()
        input("You rolled...")
        input(result)
        if result == 6:
            if height == 1:
                input(f"{climber.name} lost their footing and crashed down to the ground!")
                input(f"{climber.name} lost 10 health")
                input("You won't be eating tonight")
                Player.alter_health(climber, -10)
                return climber

            elif height == 2:
                input(f"{climber.name} lost their footing and crashed down to the ground heavily!")
                input(f"{climber.name} lost 20 health")
                input("You won't be eating tonight")
                Player.alter_health(climber, -20)
                return climber

            else:
                input(f"{climber.name} lost their footing and plummeted down to the ground, landing awkwardly!")
                input(f"{climber.name} lost 40 health")
                input("You won't be eating tonight")
                Player.alter_health(climber, -40)
                return climber

        count += 1
        height += 1

    input(f"{climber.name} made it to the top of the tree and grabbed the coconuts!")
    input("The players eat well tonight, recovering 10 health each....")
    Player.alter_health(climber, 10)
    Player.alter_health(other, 10)
    return climber, other

# Boar Hunt
def boar_hunt():
    how_close = 0
    while how_close < 4:
        choice = input("Creep closer ('C') or attack now ('A')? ")

        if choice.lower() == "c":
            if how_close == 0:
                boar_runs = roll_standard_dice()
                if boar_runs < 3:
                    input("The boar fled into the undergrowth...")
                    return "fail"
                else:
                    input("You creep closer. The boar still hasn't noticed you..")
                    how_close += 1

            elif how_close == 1:
                boar_runs = roll_standard_dice()
                if boar_runs < 4:
                    input("The boar fled into the undergrowth...")
                    return "fail"
                else:
                    input("You creep closer. The boar still hasn't noticed you..")
                    how_close += 1

            elif how_close == 2:
                boar_runs = roll_standard_dice()
                if boar_runs < 5:
                    input("The boar fled into the undergrowth...")
                    return "fail"
                else:
                    input("You creep closer. The boar still hasn't noticed you..")
                    how_close += 1

            elif how_close == 3:
                input("You can't get closer without it seeing you! Time to attack!")


        elif choice.lower() == "a":
            if how_close == 0:
                attack_success = roll_standard_dice()
                if attack_success > 4:
                    input("Success! You hit the boar and it drops to the ground!")
                    return "success"
                else:
                    input("Your attack misses and the boar flees into the undergrowth...")
                    return "fail"

            if how_close == 1:
                attack_success = roll_standard_dice()
                if attack_success > 3:
                    input("Success! You hit the boar and it drops to the ground!")
                    return "success"
                else:
                    input("Your attack misses and the boar flees into the undergrowth...")
                    return "fail"


            if how_close == 2:
                attack_success = roll_standard_dice()
                if attack_success > 2:
                    input("Success! You hit the boar and it drops to the ground!")
                    return "success"
                else:
                    input("Your attack misses and the boar flees into the undergrowth...")
                    return "fail"

            if how_close == 3:
                input("Success! You hit the boar and it drops to the ground!")
                return "success"
            else:
                input("Please enter Creep ('C') or Attack ('A')")

# Open Chest
def open_chest(player):
    input(f"Thankfully, {player.name} picked up a crowbar from the mineshaft.")
    input(f"{player.name} forces it under the edge of the chest and twists, prising it apart.")
    input("A bright light shines out, casting the cave in a golden glow. Inside is a chalice, matching the one in the etching.")
    input("Our heroes don't know what it means, but it must be important. They put it into their bag for safekeeping.")


# Rock Dodge
def rock_dodge(player, damage):
    if damage == -10:
        input(f"A rock drops towards {player.name}. Roll over 4 to dodge.")
        result = roll_dice()
        input("You rolled.......")
        input(result)
        if result > 4:
            input(f"That was a close call but {player.name} manages to dodge")
        else:
            Player.alter_health(player, damage)
            input(f"{player.name} didn't manage to get out the way and was hit by the rock. " + str(abs(damage)) + " points lost from health!")

    elif damage == -25:
        input(f"A boulder drops towards {player.name}. Roll over 3 to dodge.")
        result = roll_dice()
        input("You rolled.......")
        input(result)
        if result > 3:
            input(f"That was a close call but {player.name} manages to dodge")
        else:
            Player.alter_health(player, damage)
            input(f"{player.name} didn't manage to get out the way and was hit by the rock. " + str(abs(damage)) + " points lost from health!")

    elif damage == -50:
        input(f"Just before the summit, a massive chunk of the cave collapses and drops towards {player.name}. Roll over 2 to dodge.")
        result = roll_dice()
        input("You rolled.......")
        input(result)
        if result > 2:
            input(f"That was a close call but {player.name} manages to dodge")
        else:
            Player.alter_health(player, damage)
            input(f"{player.name} didn't manage to get out the way and was hit by the rock. " + str(abs(damage)) + " points lost from health!")



# Attack Enemy
def attack_enemy(enemy, player1, player2):
# make below a function for attack guard (associated to class?)
    result = roll_dice()
    input("You rolled.......")
    input(result)
    enemy.life -= (result + player1.weapon['attack']+ player2.weapon['attack'])
    return enemy.life


# Battle With Multiple Guards

guard1 = Guard("Guard 1")
guard2 = Guard("Guard 2")
guard3 = Guard("Guard 3")
leader = Guard_leader()

def multiple_guard_battle(player1, player2):
    alive = [guard1, guard2, guard3, leader]
    max_life = 100
    input("You can attack one enemy at a time but beware, if you don't defeat them in one hit, expect retaliation")
    while len(alive) > 0:
        count = 1
        print("Who will you attack? ")
        for guard in alive:
            print(f"{guard.name}: ({count})")
            count += 1
        selection = int(input("~ "))
        target = alive[(selection - 1)]
        attack_enemy(target, player1, player2)
        # Can easily get an error here (if someone doesn't enter 1/2/3/4). Need a way to catch one?
        if target.life <= 0: 
            alive.remove(target)
            input(f"{target.name} was defeated!")
            input("")
        else:
            if isinstance(target, Guard):
                player_hit = (Guard.random_attack_player(player1, player2))
                input(f"{target.name} survives and launches an attack on {player_hit.name}!")
                input(f"""

        {player1.name}'s health = {player1.life}/{max_life}
        {player2.name}'s health = {player2.life}/{max_life}

    """)

            else:
                player_hit = (Guard_leader.random_attack_player(player1, player2))
                input(f"{target.name} absorbs the hit and launches a brutal attack on {player_hit.name} with his mace!")
                input(f"""

        {player1.name}'s health = {player1.life}/{max_life}
        {player2.name}'s health = {player2.life}/{max_life}

    """)