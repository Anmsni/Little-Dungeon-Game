import random

gold = 0
player_hp = 15
command_player = 0
enemy_hp = 15
command_enemy = 0
enemy_list = ['Attack', 'Block']

def dungeon_game():

        player_hp = 15
        command_player = 0
        enemy_hp = 15
        command_enemy = 0
        enemy_list = ['Attack', 'Block']

        while True:
                command_player = input("PRESS KEY: 1-attack 2-block ").lower()
                if command_player == '1':
                        print("You attacked the enemy!")
                        if command_enemy == 'Block':
                                print("Your attack was blocked!")
                        else:
                                enemy_hp = enemy_hp - 5
                elif command_player == '2':
                        print("You are blocking!")
                else:
                        print("Invalid command. Please enter 1 or 2 next turn.")
                        continue

                print("----------------")
                print("The enemy has", enemy_hp, "health left.")
                print("----------------")

                if enemy_hp <= 0:
                        print("You have defeated the enemy!")
                        break
                elif player_hp <= 0:
                        print("You have been defeated!")
                        break

                command_enemy = random.choice(enemy_list)
                if command_enemy == 'Attack':
                        print("The enemy is attacking!")
                        if command_player == '2':
                                print("The enemy's attack was blocked!")
                        else:
                                player_hp = player_hp - 5
                elif command_enemy == 'Block':
                        print("The enemy did something!")
        
                print("----------------")
                print("You have", player_hp, "health left.")
                print("----------------")

                if player_hp <= 0:
                        print("You have been defeated!")
                        break
                elif enemy_hp <= 0:
                        print("You have defeated the enemy!")
                        print("You got 10 gold!")
                        break

print("Welcome to the Dungeon Game!")
print("----------------")
print("You have", player_hp, "health.")
print("An enemy appears with", enemy_hp, "health!")
print("----------------")

dungeon_game()

if player_hp > 0:
        print("----------------")
        print("Your health has been restored to 15 for the next battle.")
        print("An enemy appears with", enemy_hp, "health!")
        gold = gold + 10
        player_hp = 15
        print("----------------")
        enemy_hp = 20
else:
        print("Game Over!")
        exit()

dungeon_game()

if player_hp > 0:
        print("----------------")
        print("Hi,")
        gold = gold + 10
        print("Thank You for playing! You finished with", gold, "gold.")
        player_hp = 15
        print("----------------")
        enemy_hp = 30
else:
        print("Game Over!")
        exit()