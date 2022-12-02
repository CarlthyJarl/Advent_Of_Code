def get_file(file):
    lines = [] 
    with open(file, "r", encoding="utf8") as f:
        for line in f.read().splitlines():

            #line = int(line)
            lines.append(line)
        return lines

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


day_2()