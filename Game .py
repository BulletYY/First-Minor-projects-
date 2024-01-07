
import random
from enum import Enum

game_length = 5

game_prob = Enum("game",["Chest", "Empty"])


first_roll = {
            game_prob.Chest : 0.6,
            game_prob.Empty : 0.4
}

first_roll_keys = tuple(first_roll.keys())
first_roll_values =tuple(first_roll.values())

Colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomarańczowy',
                           'Purple': 'fiolet',
                           'Gold': 'złoty'
                          }
               )

chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }
second_roll_keys = tuple(chestColoursDictionary.keys())
second_roll_values = tuple(chestColoursDictionary.values())


gold_reward = {second_roll_keys[reward] :(reward+1) *(reward+1) *1000
               for reward in range(len(second_roll_keys))
               }

gold_aqq =0

def gain_gold_approx(value,percentage):
    min_value = value -(percentage/100)*value
    max_value = value +(percentage/100)*value
    return (random.randint(min_value,max_value))


print("sup m8 u gonna play game komnata, get it? ")

while(game_length>0):
    game_move = input("game is great so u can only move forward, get it, wanna go forward?")
    game_move = game_move.capitalize()
    if(game_move == "Yes"):
        print("great lets see what you've got")
        game_event = random.choices(first_roll_keys,first_roll_values)[0]
        if(game_event == game_prob.Chest):
            print("GREAT YOU HAVE GOT A CHEST")
            draw_color = random.choices(second_roll_keys,second_roll_values)[0]
            print("your color is", draw_color.value)
            gamer_reward =gain_gold_approx(gold_reward[draw_color],10)
            gold_aqq += gamer_reward
            print("you have got ", gold_aqq)
        elif(game_event == game_prob.Empty):
            print("unluko you have got nothing")
    else:
        print("dude, type yes u can only move forward")
        continue
        
    game_length = game_length-1

