with open("integers.txt", "r") as source_file:
    lines = source_file.readlines()

with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    