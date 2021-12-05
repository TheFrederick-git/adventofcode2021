"""1/1 adventofcode"""

with open("input.txt", "r", encoding="UTF-8") as i_file:
    data = list(map(int, i_file.read().splitlines()))
values = ["i" if data[i] > data[i - 1] else "d" for i in range(1, len(data))]
print(values.count("i"))
