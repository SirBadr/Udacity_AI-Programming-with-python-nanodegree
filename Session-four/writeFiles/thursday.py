f = open("write.txt", "r")
print(f.read())

f = open("write.txt", "a")
f.write("-- appened text")

f = open("write.txt", "r")
print(f.read())