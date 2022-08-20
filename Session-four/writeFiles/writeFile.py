#open and read the file after the appending:
f = open("write.txt", "r")
print("text before")
print(f.read())

f = open("write.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("write.txt", "r")
print("text after writing")
print(f.read())
