# work by Mahvay, WTFPL licensed
#
# you might see that I played too much Black Desert Mobile by seeing the rarity names...
#
# UPDATE 2.0: many new rarities to drop, expanded HELP command, split rarity table into parts for better readability

import random
import time
import datetime

todays_time = datetime.datetime.now().isoformat(sep=" ", timespec="seconds") # thank you StackOverflow

print("welcome to Mahvay's 'RNG Challenge (v2.0)'!")
print("datetime:", todays_time)
print(" ")

input_value = 0

decent_rolls = 0
rng_rolls = 0
crazy_rng_rolls = 0
insane_rng_rolls = 0
rng_bless_rolls = 0
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
  
print("1. press ENTER to praise RNGesus")
print("2. type 'RATES'/'rates' for rarity charts")
print("3. type 'EXIT'/'exit' to quit")
print("4. type 'STATS'/'stats' to show ongoing session stats")
print("5. type 'HELP'/'help' to show user manual")

while input_value != "EXIT" or input_value != "exit":
    input_value = input("")

    if input_value == "EXIT" or input_value == "exit":
        break
    elif input_value == 'HELP' or input_value == 'help':
        print("user manual:")
        print("1. press ENTER to praise RNGesus")
        print("2. type 'RATES'/'rates' for rarity charts")
        print("3. type 'EXIT'/'exit' to quit")
        print("4. type 'STATS'/'stats' to show ongoing session stats")
        print("5. type 'HELP'/'help' to show user manual")
        print(" ")
        print("   for HELP command, there are few variations for it:")
        print("   > 'HELP'/'help' 'decent' - shows info about DECENT rolls")
        print("   > 'HELP'/'help' 'RNG' - shows info about RNG rolls")
        print("   > 'HELP'/'help' 'crazy' - shows info about CRAZY RNG rolls")
        print("   > 'HELP'/'help' 'insane' - shows info about INSANE RNG rolls")
        print("   > 'HELP'/'help' 'blessed' - shows info about BLESSED RNG rolls")
        print("   > 'HELP'/'help' 'eternal' - shows info about ETERNAL rolls")
        print(" ")
    elif input_value == 'HELP decent' or input_value == 'help decent':
        print("following rolls qualify for DECENT roll:")
        print("> Epic")
        print("> Special")
        print("> Legendary")
        print("> Mystical")
        print(" ")
    elif input_value == 'HELP RNG' or input_value == 'help RNG':
        print("following rolls qualify for RNG roll:")
        print("> Super Special")
        print("> Extraordinary")
        print("> Abyssal")
        print("> Primal")
        print("> Extremal")
        print("> Chaos")
        print("> Ultimate")
        print("> DeathWish")
        print(" ")
    elif input_value == 'HELP crazy' or input_value == 'help crazy':
        print("following rolls qualify for CRAZY RNG roll:")
        print("> Apocalypsal")
        print("> Outer-Space")
        print("> Magical O-S")
        print("> Ultra O-S")
        print("> Transcendental")
        print("> Metaphysical")
        print("> Heavenly")
        print("> Quantum")
        print(" ")
    elif input_value == 'HELP insane' or input_value == 'help insane':
        print("following rolls qualify for INSANE RNG roll:")
        print("> Humanity's DeathWish.")
        print("> The Entire Universe")
        print("> Blessing of the Forbidden")
        print("> Incarnate's Spell")
        print("> God-like")
        print("> Infinity")
        print("> Lightness")
        print("> Impossibilism")
        print(" ")
    elif input_value == 'HELP blessed' or input_value == 'help blessed':
        print("following rolls qualify for BLESSED RNG roll:")
        print("> Supertranscendentalism")
        print(" ")
    elif input_value == 'HELP eternal' or input_value == 'help eternal':
        print("the final and the highest value is 'Eternal'. but good luck trying to get one since it's borderline impossible to do that.")
        print(" ")
    elif input_value == 'STATS' or input_value == 'stats':
        print("=== ONGOING SESSION STATS ===")
        print(" ")
        print("attempts:", attempts)
        print(" ")
        print("earned drops:")
        print("> decent:", decent_rolls)
        print("> RNG:", rng_rolls)
        print("> crazy RNG:", crazy_rng_rolls)
        print("> insane RNG:", insane_rng_rolls)
        print("> blessed RNG:", rng_bless_rolls)
        print("> eternal:", eternal_rolls)
        print(" ")
    elif input_value == "RATES" or input_value == "rates":
        print("here is your rarity chart")
        print(" ")
        print("reading guide:")
        print("<RARITY>: <BASE CHANCE>, <100 ATTEMPTS>, <1000 ATTEMPTS>, <10k ATTEMPTS>, <100k ATTEMPTS>")
        print(" ")
        print("= TYPICAL =")
        print("Ancient/Old: both 50%")
        print("Normal: 25%, 99.99%")
        print("Uncommon: 12.5%, 99.99%")
        print(" ")
        print("= RARE ONES =")
        print("Magic: 6.25%, 99.84%")
        print("Enchanted: 3.125%, 95.82%")
        print("Rare: 1.5625%, 79.30%, 99.99%")
        print("Unique: 1/128, 54.36%, 99.96%")
        print("Epic: 1/256, 32.39%, 98%")
        print("Special: 1/512, 17.76%, 85.84%")
        print(" ")
        print("= VERY RARE ONES =")
        print("Legendary: 1/1024, 9.31%, 62.36%, 99.99%")
        print("Mystical: 1/2048, 4.77%, 38.64%, 99.24%")
        print("Super Special: 1/4096, 2.41%, 21.66%, 91.30%")
        print("Extraordinary: 1/8192, 1.21%, 11.49%, 70.50%, 99.99%")
        print("Abyssal: 16.3k, 0.61%, 5.92%, 45.69%, 99.78%")
        print("Primal: 32.7k, 0.3%, 3.01%, 26.30%, 95.27%")
        print("Extremal: 65.5k, 0.15%, 1.51%, 14.15%, 78.26%")
        print(" ")
        print("= START PRAYING RNGESUS =")
        print("Ultimate: 131k, 0.08%, 0.76%, 7.35%, 53.37%")
        print("Chaos: 262k, 0.04%, 0.38%, 3.74%, 31.71%")
        print("DeathWish: 524k, 0.02%, 0.19%, 1.89%, 17.36%")
        print(" ")
        print("= PATIENCE IS THE KEY TO SUCCESS =")
        print("Apocalypsal: 1M, 0.01%, 0.1%, 0.95%, 9.1%")
        print("Outer-Space: 2M, 0.005%, 0.048%, 0.476%, 4.656%")
        print("Magical O-S: 4.1M, 0.002%, 0.024%, 0.238%, 2.356%")
        print("Ultra O-S: 8.3M, 0.001%, 0.012%, 0.119%, 1.185%")
        print(" ")
        print("= YOUR ENTER KEY WILL DIE FASTER THAN YOU DROPPING ONE OF THESE VALUES BELOW =")
        print("the rest: yes")
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
            print("+ Magic +")
            attempts += 1
            time.sleep(1)
        elif reward_result == 5:  # rate: 3.125%
            print("= Enchanted =")
            attempts += 1
            time.sleep(1)
        elif reward_result == 6:  # rate: 1.5625%
            print("-> Rare <-")
            attempts += 1
            time.sleep(1)
        elif reward_result == 7:  # rate: 1/128
            print("-=> Unique <=-")
            attempts += 1
            time.sleep(1)
        elif reward_result == 8:  # rate: 1/256
            print("->=> Epic <=<-")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 9:  # rate: 1/512
            print(">=>=> Special <=<=<")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 10:  # rate: 1/1024
            print("---------------")
            print("=> Legendary <=")
            print("---------------")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 11:  # rate: 1/2048
            print("--------------")
            print("=> Mystical <=")
            print("--------------")
            attempts += 1
            decent_rolls += 1
            time.sleep(1)
        elif reward_result == 12:  # rate: 1/4096 (RNGesus Drop)
            print("=-=-=-=-=-=-=-=-=-=-=")
            print(">>> Super Special <<<")
            print("=-=-=-=-=-=-=-=-=-=-=")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 13:  # rate: 1/8192 (RNGesus Drop)
            print("=-=-=-=-=-=-=-=-=-=-=")
            print(">>> Extraordinary <<<")
            print("=-=-=-=-=-=-=-=-=-=-=")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 14:  # rate: 16.3k (RNGesus Drop)
            print("===================")
            print(">>=<< Abyssal >>=<<")
            print("===================")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 15:  # rate: 32.7k (RNGesus Drop)
            print("==================")
            print(">>=<< Primal >>=<<")
            print("==================")
            attempts += 1
            rng_rolls += 1
            time.sleep(1)
        elif reward_result == 16:  # rate: 65.5k (Super RNGesus Drop)
            print("#=========> <##> <=========#")
            print("|       +----------+       |")
            print("| >#>#> | Extremal | <#<#< |   One in 65.5k")
            print("|       +----------+       |")
            print("#=========> <##> <=========#")
            attempts += 1
            rng_rolls += 1
            time.sleep(3)
        elif reward_result == 17:  # rate: 131k (Super RNGesus Drop)
            print("#=========> <##> <=========#")
            print("|       +----------+       |")
            print("| >#>#> | Ultimate | <#<#< |   One in 131k")
            print("|       +----------+       |")
            print("#=========> <##> <=========#")
            attempts += 1
            rng_rolls += 1
            time.sleep(3)
        elif reward_result == 18:  # rate: 262k (Super RNGesus Drop)
            print("#==> <===> <#> <===> <==#")
            print("|   >   +-------+   <   |")
            print("| >#>#> | Chaos | <#<#< |   One in 262k")
            print("|   >   +-------+   <   |")
            print("#==> <===> <#> <===> <==#")
            attempts += 1
            rng_rolls += 1
            time.sleep(3)
        elif reward_result == 19:  # rate: 524k (Super RNGesus Drop)
            print("#==> <=====> <#> <=====> <==#")
            print("|   >   +-----------+   <   |")
            print("| >#>#> | DeathWish | <#<#< |   One in 524k")
            print("|   >   +-----------+   <   |")
            print("#==> <=====> <#> <=====> <==#")
            attempts += 1
            rng_rolls += 1
            time.sleep(3)
        elif reward_result == 20:  # rate: 1M (Extreme RNGesus Drop)
            print("  #=========> <#> <=========#  ")
            print("#==> <======> <#> <======> <==#")
            print("|  ->-  +-------------+  -<-  |")
            print("| >#>#> | Apocalypsal | <#<#< |   One in 1M")
            print("|  ->-  +-------------+  -<-  |")
            print("#==> <======> <#> <======> <==#")
            print("  #=========> <#> <=========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 21:  # rate: 2M (Extreme RNGesus Drop)
            print("  #=========> <#> <=========#  ")
            print("#==> <======> <#> <======> <==#")
            print("|  ->-  +-------------+  -<-  |")
            print("| >#>#> | Outer-Space | <#<#< |   One in 2M")
            print("|  ->-  +-------------+  -<-  |")
            print("#==> <======> <#> <======> <==#")
            print("  #=========> <#> <=========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 22:  # rate: 4.1M (Extreme RNGesus Drop)
            print("  #=========> <#> <=========#  ")
            print("#==> <======> <#> <======> <==#")
            print("|  ->-  +-------------+  -<-  |")
            print("| >#>#> |   Magical   | <#<#< |   One in")
            print("| >#>#> | Outer-Space | <#<#< |   4.1M")
            print("|  ->-  +-------------+  -<-  |")
            print("#==> <======> <#> <======> <==#")
            print("  #=========> <#> <=========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 23:  # rate: 8.3M (Extreme RNGesus Drop)
            print("  #=========> <#> <=========#  ")
            print("#==> <======> <#> <======> <==#")
            print("|  ->-  +-------------+  -<-  |")
            print("| >#>#> |    Ultra    | <#<#< |   One in")
            print("| >#>#> | Outer-Space | <#<#< |   8.3M")
            print("|  ->-  +-------------+  -<-  |")
            print("#==> <======> <#> <======> <==#")
            print("  #=========> <#> <=========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 24:  # rate: 16.7M (ULTRA EXTREME RNGesus Drop)
            print("  #==========> <##> <==========#  ")
            print("#==> <=======> <##> <=======> <==#")
            print("|   -                        -    ")
            print("|  ->-  +----------------+  -<-  |")
            print("| >#>#> | Transcendental | <#<#< |   One in 16.7M")
            print("|  ->-  +----------------+  -<-  |")
            print("|   -                        -    ")
            print("#==> <=======> <##> <=======> <==#")
            print("  #==========> <##> <==========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 25:  # rate: 33.5M (ULTRA EXTREME RNGesus Drop)
            print("  #==========> <##> <==========#  ")
            print("#==> <=======> <##> <=======> <==#")
            print("|   -                        -    ")
            print("|  ->-  +----------------+  -<-  |")
            print("| >#>#> |  Metaphysical  | <#<#< |   One in 33.5M")
            print("|  ->-  +----------------+  -<-  |")
            print("|   -                        -    ")
            print("#==> <=======> <##> <=======> <==#")
            print("  #==========> <##> <==========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 26:  # rate: 67.1M (ULTRA EXTREME RNGesus Drop)
            print("  #==========> <##> <==========#  ")
            print("#==> <=======> <##> <=======> <==#")
            print("|   -                        -    ")
            print("|  ->-  +----------------+  -<-  |")
            print("| >#>#> |    Heavenly    | <#<#< |   One in 67.1M")
            print("|  ->-  +----------------+  -<-  |")
            print("|   -                        -    ")
            print("#==> <=======> <##> <=======> <==#")
            print("  #==========> <##> <==========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 27:  # rate: 134M (ULTRA EXTREME RNGesus Drop)
            print("  #==========> <#> <==========#  ")
            print("#==> <=======> <#> <=======> <==#")
            print("|   -                       -   |")
            print("|  ->-  +---------------+  -<-  |")
            print("| >#>#> |    Quantum    | <#<#< |   One in 134M")
            print("|  ->-  +---------------+  -<-  |")
            print("|   -                       -   |")
            print("#==> <=======> <#> <=======> <==#")
            print("  #==========> <#> <==========#  ")
            attempts += 1
            crazy_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 28:  # rate: 268M (RNGesus Incarnate Drop)
            print("    ========================    ")
            print("  #==========> <> <==========#  ")
            print("#==> <=======> <> <=======> <==#")
            print("|   -        - $$ -        -   |")
            print("|  ->-  +--------------+  -<-  |   +----------------+")
            print("| >#>#> |  Humanity's  | <#<#< |   |     One in     |")
            print("| >#>#> |  DeathWish.  | <#<#< |   |  >>> 268M <<<  |")
            print("|  ->-  +--------------+  -<-  |   +----------------+")
            print("|   -        - $$ -        -   |")
            print("#==> <=======> <> <=======> <==#")
            print("  #==========> <> <==========#  ")
            print("    ========================    ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 29:  # rate: 536M (RNGesus Incarnate Drop)
            print("    ========================    ")
            print("  #==========> <> <==========#  ")
            print("#==> <=======> <> <=======> <==#")
            print("|   -        - $$ -        -   |")
            print("|  ->-  +--------------+  -<-  |   +----------------+")
            print("| >#>#> |  The Entire  | <#<#< |   |     One in     |")
            print("| >#>#> |   Universe   | <#<#< |   |  >>> 536M <<<  |")
            print("|  ->-  +--------------+  -<-  |   +----------------+")
            print("|   -        - $$ -        -   |")
            print("#==> <=======> <> <=======> <==#")
            print("  #==========> <> <==========#  ")
            print("    ========================    ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 30:  # rate: 1B (RNGesus Incarnate Drop)
            print("    =============================    ")
            print("  #============> <#> <============#  ")
            print("#==> <=========> <#> <=========> <==#")
            print("|   -          - $#$ -          -   |")
            print("|  ->-  +-------------------+  -<-  |   +--------------+")
            print("| >#>#> |  Blessing of the  | <#<#< |   |    One in    |")
            print("| >#>#> |     Forbidden     | <#<#< |   |  >>> 1B <<<  |")
            print("|  ->-  +-------------------+  -<-  |   +--------------+")
            print("|   -          - $#$ -          -   |")
            print("#==> <=========> <#> <=========> <==#")
            print("  #============> <#> <============#  ")
            print("    =============================    ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 31:  # rate: 1/2147483647 (RNGesus >>> Incarnate <<< Drop)
            print("    =========================    ")
            print("  #==========> <#> <==========#  ")
            print("#==> <=======> <#> <=======> <==#")
            print("|   -        - $#$ -        -   |")
            print("|  ->-  +---------------+  -<-  |   +----------------+")
            print("| >#>#> |  Incarnate's  | <#<#< |   |     One in     |")
            print("| >#>#> |     Spell     | <#<#< |   |  >>> 2.1B <<<  |")
            print("|  ->-  +---------------+  -<-  |   +----------------+")
            print("|   -        - $#$ -        -   |")
            print("#==> <=======> <#> <=======> <==#")
            print("  #==========> <#> <==========#  ")
            print("    =========================    ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 32:  # rate: 4.2B (RNGesus' Experimental Drop)
            print("      -=-=-=-=-=--=-=-=-=-=-      ")
            print("    ==========================    ")
            print("  #==========> <##> <==========#  ")
            print("#==> <==---==> <##> <==---==> <==#   One in...")
            print("|   >    - = - $##$ - = -    <   |")
            print("|  >>>  +----------------+  <<<  |   ##  ##    ###### ######")
            print("| >#>#> |    God-like    | <#<#< |   ##  ##        ## ##  ##")
            print("|  >>>  +----------------+  <<<  |   ######    ###### ####  ")
            print("|   >    - = - $##$ - = -    <   |       ##    ##     ##  ##")
            print("#==> <==---==> <##> <==---==> <==#       ## ## ###### ######")
            print("  #==========> <##> <==========#  ")
            print("    ==========================    ")
            print("      -=-=-=-=-=--=-=-=-=-=-      ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 33:  # rate: 8.5B (RNGesus' Studies Drop)
            print("      -=-=-=-=-=--=-=-=-=-=-      ")
            print("    ==========================    ")
            print("  #==========> <##> <==========#  ")
            print("#==> <==---==> <##> <==---==> <==#   One in...")
            print("|   >    - = - $##$ - = -    <   |")
            print("|  >>>  +----------------+  <<<  |   ######    ###### ######")
            print("| >#>#> |    Infinity    | <#<#< |   ##  ##    ##     ##  ##")
            print("|  >>>  +----------------+  <<<  |   ######    ###### ####  ")
            print("|   >    - = - $##$ - = -    <   |   ##  ##        ## ##  ##")
            print("#==> <==---==> <##> <==---==> <==#   ###### ## ###### ######")
            print("  #==========> <##> <==========#  ")
            print("    ==========================    ")
            print("      -=-=-=-=-=--=-=-=-=-=-      ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 34:  # rate: 17.1B (RNGesus' First Invention Drop)
            print("      --==--==--=-=--==--==--      ")
            print("    ===========================    ")
            print("  #==========> < # > <==========#  ")
            print("#==> <==---==> < # > <==---==> <==#   One in...")
            print("|   >     - = $$ # $$ = -     <   |")
            print("|  >>>  +-----------------+  <<<  |   ####   ######    ####   ######")
            print("| >#>#> |    Lightness    | <#<#< |     ##   ##  ##      ##   ##  ##")
            print("|  >>>  +-----------------+  <<<  |     ##       ##      ##   ####  ")
            print("|   >     - = $$ # $$ = -     <   |     ##       ##      ##   ##  ##")
            print("#==> <==---==> < # > <==---==> <==#   ######     ## ## ###### ######")
            print("  #==========> < # > <==========#  ")
            print("    ===========================    ")
            print("      --==--==--=-=--==--==--      ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 35:  # rate: 34.3B (RNGesus' Greatest Invention Drop)
            print("      --==--==--=-=--==--==--      ")
            print("    ===========================    ")
            print("  #==========> < # > <==========#  ")
            print("#==> <==---==> < # > <==---==> <==#   One in...")
            print("|   >     - = $$ # $$ = -     <   |")
            print("|  >>>  +-----------------+  <<<  |   ######  ##  ##    ###### ######")
            print("| >#>#> |  Impossibilism  | <#<#< |       ##  ##  ##        ## ##  ##")
            print("|  >>>  +-----------------+  <<<  |   ######  ######    ###### ####  ")
            print("|   >     - = $$ # $$ = -     <   |       ##      ##        ## ##  ##")
            print("#==> <==---==> < # > <==---==> <==#   ######      ## ## ###### ######")
            print("  #==========> < # > <==========#  ")
            print("    ===========================    ")
            print("      --==--==--=-=--==--==--      ")
            attempts += 1
            insane_rng_rolls += 1
            time.sleep(5)
        elif reward_result == 36:  # rate: 68.7B (RNGesus' First Blessing Drop)
            print("      -=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-      ")
            print("    ====================================    ")
            print("  #==============> < ## > <==============#  ")
            print("#==> <==-==-==-==> < ## > <==-==-==-==> <==#   One in...")
            print("|   >    -= $$ ## $$ ## $$ ## $$ =-    <   |")
            print("|  >>>  +--------------------------+  <<<  |   ######  ######    ###### ######")
            print("| >#>#> |  Supertranscendentalism  | <#<#< |   ##      ##  ##    ##  ## ##  ##")
            print("|  >>>  +--------------------------+  <<<  |   ######  ######        ## ####  ")
            print("|   >    -= $$ ## $$ ## $$ ## $$ =-    <   |   ##  ##  ##  ##        ## ##  ##")
            print("#==> <==-==-==-==> < ## > <==-==-==-==> <==#   ######  ###### ##     ## ######")
            print("  #==============> < ## > <==============#  ")
            print("    ====================================    ")
            print("      -=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-      ")
            attempts += 1
            rng_bless_rolls += 1
            time.sleep(5)
        else: # rate: 137B (ULTRA EXTREME RNGesus Incarnate's Blessing Drop)
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

            print("            - - - - - -            ")
            print("          ---------------          ")
            print("        -=-=-=-=-=-=-=-=-=-        ")
            print("      =======================      ")
            print("    #=========> <#> <=========#    ")
            print("  #==> <======> <#> <======> <==#  ")
            print("#==> <=--==--=> <#> <=--==--=> <==#=================================>")
            print("|   -    $$ $$ $$ $$ $$ $$    -   |   ONE IN...                     +")
            print("$  >->  #=================#  <-<  $                                 |")
            print("| >>>>> | ^ +---------+ ^ | <<<<< |   ####   ###### ###### ######   |")
            print("$ #RNG# | ^ | Eternal | ^ | #RNG# $     ##       ## ##  ## ##  ##   |")
            print("| >>>>> | ^ +---------+ ^ | <<<<< |     ##   ######     ## ####     |")
            print("$  >->  #=================#  <-<  $     ##       ##     ## ##  ##   |")
            print("|   -    $$ $$ $$ $$ $$ $$    -   |   ###### ######     ## ######   +")
            print("#==> <=--==--=> <#> <=--==--=> <==#=================================>")
            print("  #==> <======> <#> <======> <==#  ")
            print("    #=========> <#> <=========#    ")
            print("      =======================      ")
            print("        -=-=-=-=-=-=-=-=-=-        ")
            print("          ---------------          ")
            print("            - - - - - -            ")

            print(" ")
            print("(wait 30 seconds for the RNGesus drop celebration to end)")
            print(" ")
            time.sleep(30)
            print("Make use of the blessing, because you have used your chance and are not going to get another one...")

def random_fun_fact():
    z = random.randint(0, 4)
    if z == 0:
        z1 = str("there is a way to roll the highest value. but that's borderline impossible since it's 1/137B chance.")
        return z1
    elif z == 1:
        z2 = str("there are 38 various rarities to hit. some of their names were takes straight from Black Desert Mobile and the GD level 'lets go gambling'.")
        return z2 # UPDATE THAT IF NEW RARITIES ARE GOING TO BE ADDED IN THE FUTURE!!!
    elif z == 2:
        z3 = str("the whole concept of this RNG game was inspired by the GD level 'lets go gambling' and the originator, 'Sols RNG'.")
        return z3
    elif z == 3:
        z4 = str("'Extreme RNGesus Drop' and 'ULTRA EXTREME RNGesus DROP' are references to the game 'Peggle', where hitting all the pegs would show an 'ULTRA EXTREME FEVER' message.")
        return z4
    else:
        z5 = str("this spaghetti script took now 3 hours to make. that's it.")
        return z5

print("=== SESSION SUMMARY ===")
print(" ")
print("attempts:", attempts)
print(" ")
print("earned drops:")
print("> decent:", decent_rolls)
print("> RNG:", rng_rolls)
print("> crazy RNG:", crazy_rng_rolls)
print("> insane RNG:", insane_rng_rolls)
print("> blessed RNG:", rng_bless_rolls)
print("> eternal:", eternal_rolls)
print(" ")
print("fun fact:")
print(random_fun_fact())
print(" ")

input("press ENTER to close the program")
