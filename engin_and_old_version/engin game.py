
import time
from os import system
import random
# import pdb
# pdb.set_trace()

#========================================================================================
size = int(input("enter the game size: "))
live = int(input("enter the minimum number of living homes: "))

#========================================================================================
def game_earth(x):
    first_location = {}
    for item in range(1, x+1):
        for item2 in range(1, x+1):
            first_location[(item, item2)] = [0]
    return first_location

#========================================================================================
def live_block(z, loc):
    f_list = list(loc.keys())
    s_list = []
    ran = random.randrange(len(f_list))
    
    first_random_block = random.choices(f_list, weights= None, k = z)
    for v in first_random_block:
        s_list.append(v)
    
    test = set(s_list)
    for i in test:
        f_list.remove(i)
    while(len(test) != z):
        mn = random.choice(f_list)
        f_list.remove(mn)
        s_list.append(mn)
        test = set(s_list)
    
    s_list = list(test)
    
    other_block = random.choices(f_list,weights=None, k= ran)
    for v in other_block:
        s_list.append(v)
    
    for i in loc:
        if i in s_list:
            loc[i] = [1]

    return loc

#========================================================================================
def draw(x):
    global size
    counterr = 1
    system("cls")
    for i in x:
        if (counterr%size) == 0:
            print(x[i][0])
            #if x[i][0] == 0:
            #   print("□")
            #else:
            #   print("█")
        else:
            print(x[i][0], end="")
            #if x[i][0] == 0:
            #   print("□", end="")
            #else:
            #   print("█", end="")
        counterr +=1

#========================================================================================
def erea(x, n):
    list_hamsaye = []
    z = list(n)
    for i in range(1, 4):
        for cc in range(1, 4):
            f = [z[0]+(i-2), z[1]+(cc-2)]
            if tuple(f) in x:
                list_hamsaye.append(tuple(f))
    list_hamsaye.remove(n)
    return list_hamsaye

#========================================================================================
def sabet_erea(x):
    dict_sabet = {}
    for i in x:
        z = erea(x, i)
        dict_sabet[i] = z
    return dict_sabet

#========================================================================================
def tagirat(x):
    global save_locations
    new_locations = save_locations.copy()
    for i in x:
        vb = dict_sabet[i]
        live = 0
        dead = 0
        for z in vb:
            if x[z] == [1]:
                live += 1
            else:
                dead += 1
        if (live == 2) or (live == 3):
            new_locations[i] = [1]
        else:
            new_locations[i] = [0]
    return new_locations

#========================================================================================
z1 = time.process_time()
print("Building the playground for the first time, please wait.")
locations = game_earth(size)
save_locations = locations.copy()
dict_sabet = sabet_erea(locations)
locations = live_block(live, locations)
draw(locations)
print("\n ")
z2 = time.process_time()
print(z2-z1)
input("this is the first case, Enter a key to continue: ")

for i in range(1, 100):
    # input()
    x1 = time.process_time()
    time.sleep(1)
    locations = tagirat(locations)
    draw(locations)
    print("\n \n", "in step ", i)
    x2 = time.process_time()
    print(x2-x1)
    