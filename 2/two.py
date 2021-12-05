"""2/2 adventofcode"""

with open("input.txt", "r", encoding="UTF-8") as i_file:
    data = i_file.read().splitlines()
submarine = [0, 0]
aim = 0
for line in data:
    value = int(line.split(" ")[1])
    match line.split(" ")[0]:
        case "up":
            aim -= value
        case "down":
            aim += value
        case "forward":
            submarine[0] += value
            submarine[1] += value*aim
print(submarine[0]*submarine[1])
