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

# CREATE A DICTIONARY
d={"name":"sukesh","age":20,"dept":"CSE"}
if "name" in d:
    print("found")
else:
    print("not found")
    
#frequency of digit
l = [1,2,2,3,3,3,4,4,4,4]
freq = {}
for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#frequency of string
s="python is easy python is amazing"
words = s.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

#Merge two dict
a={"a":1}
b={"b":2}
a.update(b)
print(a)