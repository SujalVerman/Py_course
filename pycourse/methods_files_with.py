# f = open("bye.txt")
# line = f.read()
# print(line)
# f.close()

# Same can be written as with < with > statement:

with open("bye.txt") as f:
    print(f.read())
# We don't need to close the file or f.close()