# {key1:value1, key2:value2, key3:value3, key4:value4, ...}
elements = {"hydrogen": [1, 2, 4], "helium": 2.5, "carbon": "String"}


#print(elements["helium"])
#elements["helium"] = 3 
#print(elements["helium"])

#print(elements["lithium"])
#print(elements.get("liohthimfdf"))


#print("carbon" in elements)
#print("lithhium" in elements)
#print(elements.get("dilithium"))


n = elements.get("dilithium")
print(n is None)
print(n  == None)
#print(n is not None)