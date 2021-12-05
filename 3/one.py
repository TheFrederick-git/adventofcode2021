"""3/1 adventofcode"""

with open("input.txt", "r", encoding="UTF-8") as i_file:
    data = i_file.read().splitlines()
columns = [[row[i] for row in data] for i in range(len(data[0]))]

def binlst_to_int(values) -> int:
    """Returns int values of binary in list form"""
    values = values[::-1]
    total = 0
    for i in range(len(values)):
        total += values[i]*2**i
    return total

def get_most(columns) -> list:
    """Returns list of most common values for each column"""
    return [1 if column.count("1") > column.count("0") else 0 for column in columns]

def get_least(columns) -> list:
    """Returns list of least common values for each column"""
    return [0 if column.count("0") < column.count("1") else 1 for column in columns]

print(binlst_to_int(get_most(columns))*binlst_to_int(get_least(columns)))
