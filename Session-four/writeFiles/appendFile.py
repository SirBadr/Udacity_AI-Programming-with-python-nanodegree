#open and read the file after the appending:
f = open("write.txt", "r")
print("text before")
print(f.read())

f = open("write.txt", "a")
f.write("Woops! I have appended to the content!")
f.close()

#open and read the file after the appending:
f = open("write.txt", "r")
print("text after writing")
print(f.read())
