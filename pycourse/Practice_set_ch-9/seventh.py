
word ="python"
with open("log.txt", "r") as f:
    const = f.readlines()
lineno = 1
for line in const:
    if(word in line):
        print(f"Yes the {word} is present in log file in line no:{lineno}")
        
    lineno +=1