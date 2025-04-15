# This will create a file or overwrite if it exists
with open("example.txt", "w") as file:
    file.write("Hello, this is my first file!\n")
    file.write("File handling is easy in Python.\n")

# This adds to the file without deleting existing content
with open("example.txt", "a") as file:
    file.write("This line is added later.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newlines

with open("example.txt", "r") as file:
    lines = file.readlines()  # returns a list of lines
    print(lines)



