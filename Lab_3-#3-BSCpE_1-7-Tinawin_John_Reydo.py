with open ("gwa.txt", "r") as gwa_file:
    highest_name = ""
    highest_gwa = float("inf")

    for line in gwa_file.readlines():
        name, gwa = line.strip().split(",")
        