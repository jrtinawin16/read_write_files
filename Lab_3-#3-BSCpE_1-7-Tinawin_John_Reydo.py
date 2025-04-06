with open ("gwa.txt", "r") as gwa_file:
    highest_name = ""
    highest_gwa = float("inf")

    for line in gwa_file.readlines():
        student_name, student_gwa = line.strip().split(",")
        student_gwa = float(student_gwa)
        if student_gwa < highest_gwa:
            highest_gwa = student_gwa
            highest_name = student_name

print("Student with Highest GWA: " + (highest_name))
print("GWA: ", highest_gwa)