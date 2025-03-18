# work by Mahvay, WTFPL licensed
#
# you might see that I played too much Black Desert Mobile by seeing the rarity names...
#
# UPDATE 1.1: added rarity chart! now you can estimate how much time you will waste trying to drop a very high roll value!

import random
import time
import datetime

todays_time = datetime.datetime.now().isoformat(sep=" ", timespec="seconds") # thank you StackOverflow

print("welcome to Mahvay's 'RNG Challenge (v1.1)'!")
print("datetime:", todays_time)
print(" ")

input_value = 0

decent_rolls = 0
rng_rolls = 0
eternal_rolls = 0

attempts = 0

def RNGchall():
  y = 0  # boot-up value
  while True:
    x = random.randint(0, 1)
    if x == 0:
      break  # exit the loop if 0 is rolled
    else:
      y += 1  # add dopamine if 1 is rolled
  return y

while input_value != "EXIT" or input_value != "exit":
    print("press ENTER to praise RNGesus, type 'RATES'/'rates' for rarity charts or type 'EXIT'/'exit' to quit")
    input_value = input("")

    if input_value == "EXIT" or input_value == "exit":
        break
    elif input_value == "RATES" or input_value == "rates":
        print("here is your rarity chart")
        print(" ")
        print("reading guide:")
        print("<RARITY>: <BASE CHANCE>, <100 ATTEMPTS>, <1000 ATTEMPTS>, <10k ATTEMPTS>, <100k ATTEMPTS>")
        print(" ")
        print("Ancient/Old: both 50%")
        print("Normal: 25%, 99.99%")
        print("Uncommon: 12.5%, 99.99%")
        print("Magic: 6.25%, 99.84%")
        print("Rare: 3.125%, 95.82%")
        print("Unique: 1.5625%, 79.30%, 99.99%")
        print("Epic: 1/128, 54.36%, 99.96%")
        print("Special: 1/256, 32.39%, 98%")
        print("Legendary: 1/512, 17.76%, 85.84%")
        print("Mystical: 1/1024, 9.31%, 62.36%, 99.99%")
        print("Super Special: 1/2048, 4.77%, 38.64%, 99.24%")
        print("Abyssal: 1/4096, 2.41%, 21.66%, 91.30%")
        print("Primal: 1/8192, 1.21%, 11.49%, 70.50%, 99.99%")
        print("Ultimate: 16.3k, 0.61%, 5.92%, 45.69%, 99.78%")
        print("Chaos: 32.7k, 0.3%, 3.01%, 26.30%, 95.27%")
        print("DeathWish: 65.5k, 0.15%, 1.51%, 14.15%, 78.26%")
        print("Eternal: 131k, 0.08%, 0.76%, 7.35%, 53.37%")
        print(" ")
    else:
        reward_result = RNGchall()

        print("rolled value:")

        if reward_result == 0:  # rate: 50%
            print("Ancient")
            attempts += 1
            time.sleep(1)
        elif reward_result == 1:  # rate: 50%
            print("Old")
            attempts += 1
            time.sleep(1)
        elif reward_result == 2:  # rate: 25%
            print("Normal")
            attempts += 1
            time.sleep(1)
        elif reward_result == 3:  # rate: 12.5%
            print("- Uncommon -")
            attempts += 1
            time.sleep(1)
        elif reward_result == 4:  # rate: 6.25%
            print("= Magic =")
            attempts += 1
            time.sleep(1)
        elif reward_result == 5:  # rate: 3.125%
            print("-> Rare <-")
            attempts += 1
            time.sleep(1)
        elif reward_result == 6:  # rate: 1.5625%
            print("-=> Unique <=-")
            attempts += 1
            time.sleep(1)
        elif reward_result == 7:  # rate: 1/128
            print("->=> Epic <=<-")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 8:  # rate: 1/256
            print(">=>=> Special <=<=<")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 9:  # rate: 1/512
            print("---------------")
            print("=> Legendary <=")
            print("---------------")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 10:  # rate: 1/1024
            print("--------------")
            print("=> Mystical <=")
            print("--------------")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 11:  # rate: 1/2048 (RNGesus Drop)
            print("=-=-=-=-=-=-=-=-=-=-=")
            print(">>> Super Special <<<")
            print("=-=-=-=-=-=-=-=-=-=-=")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 12:  # rate: 1/4096 (RNGesus Drop)
            print("=-=-=-=-=-=-=-=")
            print(">>> Abyssal <<<")
            print("=-=-=-=-=-=-=-=")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 13:  # rate: 1/8192 (Super RNGesus Drop)
            print("==================")
            print(">>=<< Primal >>=<<")
            print("==================")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 14:  # rate: 16.3k (Super RNGesus Drop)
            print("====================")
            print(">>=<< Ultimate >>=<<")
            print("====================")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 15:  # rate: 32.7k (Extreme RNGesus Drop)
            print("#========> <#> <========#")
            print("|       +-------+       |")
            print("| >#>#> | Chaos | <#<#< |")
            print("|       +-------+       |")
            print("#========> <#> <========#")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 16:  # rate: 65.5k (Extreme RNGesus Drop)
            print("#==========> <#> <==========#")
            print("|       +-----------+       |")
            print("| >#>#> | DeathWish | <#<#< |")
            print("|       +-----------+       |")
            print("#==========> <#> <==========#")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        else: # rate: 131k (ULTRA EXTREME RNGesus DROP)
            attempts += 1
            eternal_rolls += 1
            time.sleep(5)
            print("You feel an unknown energy flowing in your mind...")
            time.sleep(10)
            print("It just flows... but it doesn't make you uncomfortable...")
            time.sleep(10)
            print("You feel happiness and you start feeling like you are only 16 again...")
            time.sleep(7)
            print("...because it's some kind of energy, a positive energy.")
            time.sleep(10)
            print("You start seeing random things that exist in the Universe...")
            time.sleep(5)
            print("The levitation slowly sends you off the Earth...")
            time.sleep(5)
            print("To the point where you are able to see your entire real world and the outside of it...")
            time.sleep(10)
            print("You then realize what just happened. The energy wasn't just a new power...")
            time.sleep(5)
            print("It was a blessing. A very rare one...")
            time.sleep(10)
            print("Physical Eternity welcomes you...")
            print(" ")

            print("#==> <=--==--=> <#> <=--==--=> <==#")
            print("|   -    $$ $$ $$ $$ $$ $$    -   |   ONE IN...")
            print("$  >->  #=================#  <-<  $")
            print("| >>>>> | ^ +---------+ ^ | <<<<< |   ####   ###### ####   ##    ")
            print("$ #RNG# | ^ | Eternal | ^ | #RNG# $     ##       ##   ##   ##    ")
            print("| >>>>> | ^ +---------+ ^ | <<<<< |     ##   ######   ##   ##  ##")
            print("$  >->  #=================#  <-<  $     ##       ##   ##   ####  ")
            print("|   -    $$ $$ $$ $$ $$ $$    -   |   ###### ###### ###### ##  ##")
            print("#==> <=--==--=> <#> <=--==--=> <==#")

            print(" ")
            print("(wait 30 seconds for the RNGesus drop celebration to end)")
            print(" ")
            time.sleep(30)
            print("Make use of the blessing, because you have used your chance and are not going to get another one...")

def random_fun_fact():
    z = random.randint(0, 4)
    if z == 0:
        z1 = str("it is possible to roll an 'ULTRA EXTREME RNGesus DROP'. but it's extremely rare since it's 1/131k chance.")
        return z1
    elif z == 1:
        z2 = str("there are 18 various rarities to hit. some of their names were takes straight from Black Desert Mobile and the GD level 'lets go gambling'.")
        return z2 # UPDATE THAT IF NEW RARITIES ARE GOING TO BE ADDED IN THE FUTURE!!!
    elif z == 2:
        z3 = str("the whole concept of this RNG game was inspired by the GD level 'lets go gambling' and the originator, 'Sols RNG'.")
        return z3
    elif z == 3:
        z4 = str("'Extreme RNGesus Drop' and 'ULTRA EXTREME RNGesus DROP' are references to the game 'Peggle', where hitting all the pegs would show an 'ULTRA EXTREME FEVER' message.")
        return z4
    else:
        z5 = str("this spaghetti script took an hour to make and another hour to format the small ASCII arts.")
        return z5

print("=== SESSION SUMMARY ===")
print(" ")
print("attempts:", attempts)
print(" ")
print("earned drops:")
print("> decent:", decent_rolls)
print("> RNG:", rng_rolls)
print("> eternal:", eternal_rolls)
print(" ")
print("fun fact:")
print(random_fun_fact())
print(" ")

input("press ENTER to close the program")
