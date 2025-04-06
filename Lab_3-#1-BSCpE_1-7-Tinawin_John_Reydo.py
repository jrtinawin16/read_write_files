with open("mylife.txt", "w") as myFile:
    while True:
        ask_line = input("Enter line: ")
        myFile.write(ask_line + "\n")
        ask_more = input("Are there more lines? (y/n): ").strip().lower()
        if ask_more != "y":
            break