with open("This_copy.txt", "r") as f:
    content1 = f.read()
with open("this.txt", "r") as f:
    content2 = f.read()
if(content1 == content2):
    print("Yes it is identical!")
else:
    print("Not indentical!")