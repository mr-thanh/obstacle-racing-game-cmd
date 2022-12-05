import subprocess
import random
import time
import keyboard

# create array of road and lines
borderline = [
    ['+', '|', '+'],
    ['|', ' ', '|'],
    ['|', '|', '|'],
    ['+', ' ', '+'],
    ['|', '|', '|'],
    ['|', ' ', '|'],
    ['+', '|', '+'],
    ['|', ' ', '|'],
    ['|', '|', '|'],
    ['+', ' ', '+'],
    ['|', '|', '|'],
    ['|', ' ', '|'],
    ['+', ' ', '+'],
    ['|', '|', '|'],
    ['|', ' ', '|']
]
main_road = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   ']
]

# some variables
car_pos = 1
car = '_^_'
right = "right"
left = "left"
level = 0
score = 0

# create obstacles randomly
def obstacle():
    temp = [
        ['   ', '   ', ' = '],
        ['   ', ' = ', '   '],
        [' = ', '   ', '   '],
        [' = ', '   ', ' = '],
        [' = ', ' = ', '   '],
        ['   ', ' = ', ' = '],
    ]
    return random.choice(temp)

# create an iterator object which make 3 blank road and
# 1 obstacle road alternately
def alternate():
    while True:
        yield ['   ', '   ', '   ']
        yield ['   ', '   ', '   ']
        yield ['   ', '   ', '   ']
        yield obstacle()
alternator = alternate()

# function to shift a list or array to right
# (it looks like a road running)
# and this function used to shift borderline
def shift_to_right(list_):
    temp = list_[-1]
    for i in range(len(list_) - 1, 0, -1):
        list_[i] = list_[i - 1]
    list_[0] = temp

# this fucntion is similar to above
# it applied to road (main_road)
def road_run(list_):
    for i in range(len(list_) - 1, 0, -1):
        list_[i] = list_[i - 1]
    list_[0] = next(alternator)
    if list_[-4][car_pos] == ' = ':
        print("\nDo You want to replay? [y]es or [n]o")
        while True:
            if keyboard.is_pressed('y'):
                start_game()
            if keyboard.is_pressed('n'):
                exit()

# function to move car object
def move(left_right):
    global car_pos
    if left_right == right and car_pos < 2:
        car_pos += 1
    if left_right == left and car_pos > 0:
        car_pos -= 1

# display all of things to screen
def display():
    subprocess.run("cls", shell=True)
    print("   -----------------")
    for i in range(len(borderline) - 4):
        print('     ', borderline[i][0], main_road[i][0],borderline[i][1], main_road[i][1],
              borderline[i][1], main_road[i][2], borderline[i][2],
              f'    MINI GAME - Obstacle Racing' if i == 0 else '',
              f'    ---------------------------' if i == 1 else '',
              f'    LEVEL {level} - SCORE {score}' if i == 2 else '',
              f'    ---------------------------' if i == 3 else '',
              f'    [LEFT] to Left - [RIGHT] to Right' if i == 4 else '',
              f'    ---------------------------' if i == 5 else '',
              f'    Press [P]/[O] to pause/continue' if i == 6 else '',
              f'    Press [Q] to quit' if i == 7 else '',
              f'    ---------------------------' if i == 8 else '',
              f'    Mr.Thanh' if i == 9 else '',
              f'    www.youtube.com/anhkythuatchannel' if i == 10 else '',
              sep='')
    if car_pos == 0:
        temp = car + borderline[-4][1] + main_road[-4][1] + borderline[-4][1] + main_road[-4][2]
    elif car_pos == 1:
        temp = main_road[-4][0] + borderline[-4][1] +  car + borderline[-4][1] + main_road[-4][2]
    else:
        temp = main_road[-4][0] + borderline[-4][1] + main_road[-4][1] + borderline[-4][1] + car
    print('     ', borderline[-4][0], temp, borderline[-4][2], sep='')
    for i in range(-3,0,1):
        print('     ', borderline[i][0], main_road[i][0],borderline[i][1], main_road[i][1],
              borderline[i][1], main_road[i][2], borderline[i][2],sep='')

# check event keyboard
def check_key():
    if keyboard.is_pressed(left):
        move(left)
        time.sleep(0.01)
    if keyboard.is_pressed(right):
        move(right)
        time.sleep(0.01)
    if keyboard.is_pressed('q'):
        exit()
    if keyboard.is_pressed('p'):
        while True:
            if keyboard.is_pressed('o'):
                break
            if keyboard.is_pressed('q'):
                exit()

# main function to start game
def start_game():
    global level, car_pos, main_road, score
    main_road = [
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   ']
    ]
    car_pos = 1
    level = 0
    # n is the speed, n is as small, the speed as fast
    n = 6
    score = 0
    while True:
        for count in range(20):
            if count % 5 == 0 and count != 0:
                score += 5
            for i in range(n):
                check_key()
                display()
                time.sleep(0.01)
            road_run(main_road)
            shift_to_right(borderline)
        level += 1
        if n > 0: n -= 1

start_game()











