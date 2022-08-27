#open and read the file after the appending:
f = open("write.txt", "r")
print("text before")
print(f.read())

f = open("write.txt", "a")
f.write("my appended text")
f.close()

#open and read the file after the appending:
f = open("write.txt", "r")
print("text after writing")
print(f.read())
