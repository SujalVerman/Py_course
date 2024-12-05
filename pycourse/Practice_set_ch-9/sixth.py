word ="python"
with open("log.txt", "r") as f:
    const = f.read()
    if(word in const):
        print(f"Yes the {word} is present in log file")
    else:
        print(f"not present")
