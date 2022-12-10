from string import ascii_letters
import numpy as np


def get_file(file):
    lines = [] 
    with open(file, "r", encoding="utf8") as f:
        for line in f.read().splitlines():

            #line = int(line)
            lines.append(line)
        return lines

def get_file2(file):
    with open(file) as f:
        return [i for i in f.read().strip().split("\n")]

def get_file3(file):
    with open(file, "r") as fin:
        return fin.read().strip().split()

def how_to_letters():
    for num, letter in enumerate(ascii_letters):
        print(num, letter)
        

def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2
    # mystring = 'SplitWords'
    # print('My string',mystring)
    # print('Split the string into two:',splitstring(mystring))

def day_1():
    lines, list_of_stuf, num, = [], [], 0
    with open("2022_day1.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():

            #line = int(line)
            lines.append(line)

        #print(lines)

        for i in lines:
            if i == '':
                list_of_stuf.append(num)
                num = 0
            else:
                num += int(i)
                
        list_of_stuf.sort()
        print(list_of_stuf[-1] + list_of_stuf[-2] + list_of_stuf[-3])

#day_1()


def day_2():
    rounds = get_file("2022_day2.txt")
    #print(rounds)

    for i, v in enumerate(rounds):
        #print(i, v)
        pass

# For my sanety lol
# ---------------------------------------------
# LEFT VS RIGHT | OUT | RIGHT + OUTCOME = TOTAL
# ---------------------------------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN  = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN  = (3 + 6) = 9
# C vs X = WIN  = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

    outcomes = {
        "A X":4, "A Y": 8, "A Z": 3,
        "B X":1, "B Y": 5, "B Z": 9,
        "C X":7, "C Y": 2, "C Z": 6
    }

    total_points_p1 = 0
    for round in rounds:
        total_points_p1 += outcomes[round]

 

    outcomes_part2 = {
        "A X":3, "A Y": 4, "A Z": 8,
        "B X":1, "B Y": 5, "B Z": 9,
        "C X":2, "C Y": 6, "C Z": 7
    }
    
    total_points_p2 = 0
    for round in rounds:
        total_points_p2 += outcomes_part2[round]

   # Answers
    print("Answers part 1:", total_points_p1)
    print("Answers part 1:", total_points_p2)


#day_2()

def day_3():
    input = get_file2("2022_day3.txt")

    # new_list = []
    # for i in input:
    #     words = splitstring(i)
    #     new_list.append(words[0])
    #     new_list.append(words[1])

    # for j in new_list:
    #     for l in range(0, len(new_list[j])):
    #         print(l)

    tot = 0
    for i in input:
        # Halvans längd
        half = len(i)//2

        left = set(i[:half])
        right = set(i[half:])

        #print(i, left, right)

        for num, letter in enumerate(ascii_letters):
            if letter in left and letter in right:
                tot += num + 1

    print(tot)


    num2 = 3
    tot = 0
    for i in range(0, len(input), 3):
        list_of_3 = input[i:num2]
        num2 += 3

        #print(list_of_3)

        for num, letter in enumerate(ascii_letters):
            if letter in list_of_3[0] and letter in list_of_3[1] and letter in list_of_3[2]: # ksk kan göra en for loop
                tot += num + 1

    print(tot)

#day_3()


def day_4():
    pass

def day_8():
    trees = get_file2("2022_day8.txt")

    #print(trees)

    grid = [list(map(int, list(trees))) for tree in trees]
    #print(grid)

    lenth_n = len(grid)
    lenth_m = len(grid[0])

    grid = np.array(grid) #vene vad denna gör tbh 
    #print(grid)

    visible_trees = 0
    for i in range(lenth_n):
        for j in range(lenth_m):
            hight = grid[i ,j]

            if j == 0 or np.amax(grid[i, :j]) < hight:
                visible_trees += 1
            elif j == lenth_m - 1 or np.amax(grid[i, (j+1):]) < hight:
                visible_trees += 1
            elif i == 0 or np.amax(grid[:i, j]) < hight:
                visible_trees += 1
            elif i == lenth_n - 1 or np.amax(grid[(i+1):, j]) < hight:
                visible_trees += 1

    #print(visible_trees)
    # no workig :(


day_8()

