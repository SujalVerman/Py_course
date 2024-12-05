with open("poem.txt") as f:
    content = f.read()
    if("twinkle" in content):
        print("Twinkle is present in content")
    else:
        print("Twinkle is not present in content")