import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np



def day1_2021():
    things, things2, num = [], [], 0
    with open("day1.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():

            line = int(line)
            things.append(line)

            #number = len(things)
            
        for i in range(len(things)):
            #print(i)
            things2.append(things[i-2]+things[i-1]+things[i])
            #print(things[i])
            if things2[i-1] < things2[i]:
                num += 1
            else:
                continue
    print(num)
    #print(things)


#day1_2021()

def day2_2021():
    things = []
    with open("2021_day2.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            things.append(line)

        horizontal = 0
        vertical = 0

        for i in range(len(things)):
            if "forward" in things[i]:
                horizontal += int((re.findall(r'\d+',things[i])[0]))

            elif "up" in things[i]:
                vertical -= int((re.findall(r'\d+',things[i])[0]))

            elif "down" in things[i]:
                vertical += int((re.findall(r'\d+',things[i])[0]))

        print(horizontal*vertical)
        
#day2_2021()

def day2_part2_2021():
    # lines = []
    with open("2021_day2.txt", "r", encoding="utf8") as f:
        # for line in f.read().splitlines():
        #     lines.append(line)
        lines = f.readlines()
        commands = [entry.strip() for entry in lines]

        horizontal, depth, aim = 0, 0, 0
        for command in commands:
            direction, amount = command.split(' ')[0], int(command.split(' ')[1])
            if "forward" in direction:
                horizontal += amount
                depth += aim * amount
            elif "up" in direction: 
                aim -= amount
            elif "down" in direction:
                aim += amount

    print(horizontal * depth)

#day2_part2_2021()


def day1_part1_and_2_2020():
    lines = []
    with open("2020_day1.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            line = int(line)
            lines.append(line)

        #print(lines)

        # for i in range(len(lines)): 
        #     for j in range(len(lines)):
        #         if lines[i] + lines[j] == 2020:
        #             print(lines[i] * lines[j]) #förstår ej varför detta inte funkar

        for i in lines:
            if 2020-i in lines:
                print(i*(2020-i))

        #part2

        for i in lines:
            for j in lines:
                if (2020-i - j) in lines:
                    print(2020-i -j, i, j)

#day1_part1_and_2_2020()


def day2_part_1_and_2_2020():

    with open("2020_day2.txt", "r", encoding= "utf8") as f:
        valid = 0
        for line in f.readlines():
            info = line.split(" ")

            amount = [info[0].split("-")]
            count = 0
            for char in info[2]:
                if char == info[1].replace(":", ""):
                    count += 1
                    print(amount)
            if count >= int(amount[0][0]) and count <= int(amount[0][1]):
                valid += 1

    print(valid)


day2_part_1_and_2_2020()


def day2019():
    with open( f"2019_day1.txt", "r") as f:
        a = f.readlines()
        b = []
        for c in a:
            b.append(int(c.strip("\n")))
    matrix_input = np.array(b)
    output = np.sum(np.floor(matrix_input / 3) - 2)
    print(output)


    with open( f"2019_day1.txt", "r") as f:
        a = f.readlines()
        b = []
        for c in a:
            b.append(int(c.strip("\n")))

    total_fuel = 0

    for mod in b:
        new_fuel = mod

        while True:
            new_fuel = np.floor(new_fuel / 3) - 2
            if new_fuel > 0:
                total_fuel += new_fuel
            else:
                break

    print(total_fuel)

#day2019()


"""
Coola grejer 
https://www.youtube.com/watch?v=OI81yqgRWGc 
https://www.youtube.com/watch?v=29zeu0lBjOI
https://www.youtube.com/watch?v=jWUdZuOU3Uc 
https://dev.to/qviper/advent-of-code-2020-python-solution-day-1-16cd
https://www.youtube.com/watch?v=dQw4w9WgXcQ 

    
"""



def lol():
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string').click()

#lol()