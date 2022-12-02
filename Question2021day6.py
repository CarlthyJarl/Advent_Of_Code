def import_file(file):
    lines = []    
    with open(file, "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            #line = int(line)
            lines.append(line)
        return lines


def do_things():
    lines = import_file("2021_day6.txt")

    print(lines)

#do_things()


def import_puzzle(location):
    with open(location, "rt") as f:
        return [int(entry) for entry in f.readline().split(",")]


def part_one(fishes):
    fish_timers = list(fishes)
    days = 80

    for _ in range(days):
        new_fish = []                           # lista för alla nya fiskar
        for fish in enumerate(fish_timers):
            fish_timers[fish[0]] -= 1           # ta bort en dag från timern
            if fish_timers[fish[0]] == -1:      # är det dags att yngla av sig?
                new_fish.append(8)              # skapa en ny fisk med timer 8
                fish_timers[fish[0]] = 6        # ändra mig till timer 6
        fish_timers.extend(new_fish)            # lägg på de nya fiskarna på de gamla
    return len(fish_timers)

if __name__ == "__main__":
    fishes = import_puzzle("2021_day6.txt")
    print(part_one(fishes))