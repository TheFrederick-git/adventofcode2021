"""1/2 adventofcode"""

with open("input.txt", "r", encoding="UTF-8") as i_file:
    data = list(map(int, i_file.read().splitlines()))
results = [data[i] + data[i + 1] + data[i + 2] for i in range(0, len(data) - 2)]
values = ["i" if results[i] > results[i - 1] else "d" for i in range(1, len(results))]
print(values.count("i"))
