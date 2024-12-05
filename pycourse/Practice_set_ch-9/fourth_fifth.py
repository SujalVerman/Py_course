word = ["donkey","is"]
with open("fourth.txt", "r") as f:
    content = f.read()
for words in word:
    content = content.replace(words, "#"*len(words))
with open("fourth.txt", "w") as f:
    f.write(content)