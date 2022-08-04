# {key1:value1, key2:value2, key3:value3, key4:value4, ...}
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])
elements["lithium"] = 3 
print(elements["lithium"])

print("carbon" in elements)
print(elements.get("dilithium"))


n = elements.get("dilithium")
print(n is None)
print(n is not None)