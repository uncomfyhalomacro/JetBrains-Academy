import random

moves = ['rock', 'fire', 'snake', 'scissors', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
         'devil', 'lightning', 'gun']
classic = ['rock', 'paper', 'scissors']
strong_against = {'rock': moves[1:8], 'fire': moves[2:9], 'snake': moves[3:10], 'scissors': moves[4:11],
                  'human': moves[5:12], 'tree': moves[6:13],
                  'wolf': moves[7:14], 'sponge': moves[8:15], 'paper': moves[9:] + moves[0:1],
                  'air': moves[10:] + moves[0:2], 'water': moves[11:] + moves[0:3],
                  'dragon': moves[12:] + moves[0:4], 'devil': moves[13:] + moves[0:5],
                  'lightning': moves[14:] + moves[0:6], 'gun': moves[0:7]}


with open('rating.txt', 'r+') as scores:
    random.seed(0)
    list_scores = []
    player_name = input('Enter your name: ')
    print(f'Hello, {player_name}')
    list_scores = []
    for _ in scores:
        list_scores.append(_.replace('\n', ''))

    list_scores = [x.split() for x in list_scores]
    for names in range(0, len(list_scores)):
        if player_name in list_scores[names]:
            break
    else:
        list_scores.append([player_name, 0])

custom = input().split(',')
if custom == ['']:
    custom = ['rock', 'paper', 'scissors']
else:
    custom = custom

print("Okay, let's start")

while True:
    computer = random.choice(custom)
    choose = input()
    trash = strong_against[computer]

    if choose in trash and choose in custom:
        print(f'Sorry, but computer chose {computer}')

    elif choose == computer:
        print(f'There is a draw {computer}')
        for add_rate1 in range(0, len(list_scores)):
            if list_scores[add_rate1][0] == player_name:
                list_scores[add_rate1][1] = int(list_scores[add_rate1][1]) + 50
            else:
                continue

    elif choose == '!exit':
        print('Bye!')
        break

    elif choose == '!rating':
        for rate in range(0, len(list_scores)):
            if list_scores[rate][0] == player_name:
                print('Your rating:', list_scores[rate][1])
            else:
                continue

    elif choose not in trash and choose in custom:
        print(f'Well done. Computer chose {computer} and failed')
        for add_rate2 in range(0, len(list_scores)):
            if list_scores[add_rate2][0] == player_name:
                list_scores[add_rate2][1] = int(list_scores[add_rate2][1]) + 100
            else:
                continue
    else:
        print('Invalid input')

with open('rating.txt', 'w+') as update:
    for player_rating in list_scores:
        print(*player_rating, file=update, sep=' ', flush=True)
