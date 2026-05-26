# CREATE A DICTIONARY
d={"name":"sukesh","age":20,"dept":"CSE"}
print(d)

#add key value
d["grade"] = 9.6
d.update({"year": 2})
print(d)

# update dict
d["grade"]=9.54
print(d)

#remove element
d.pop("year")
del d["grade"]
print(d)

#iteration in dict
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(f"{key}:{value}")