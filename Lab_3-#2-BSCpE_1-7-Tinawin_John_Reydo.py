with open("integers.txt", "r") as source_file:
    lines = source_file.readlines()

with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    for line in lines:
        for value in line.split():
            number = int(value)
            if number % 2 == 0:
                double_file.write(str(number ** 2) + "\n")
            else:
                triple_file.write(str(number ** 3) + "\n")