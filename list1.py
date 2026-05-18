## sum of numbers
l=[1,2,3,4]
sum =0;
for x in l:
    sum = sum +x
print(sum)

## max and similay way of min
max = 0
l=[1,2,3,4,5]
for x in l:
    if x > max:
        max = x
print(max)

# reverse of list
l=[1,2,3,4]
rev =[]
for x in range(len(l)-1,-1,-1):
    rev.append(l[x])
print(rev)

# element exist
l=[1,2,3,4]
x=30
if x in l:
    print("found")
else:
    print("not found")


# count of even and odd
l=[1,2,3,4,5]
even = 0
odd = 0
for x in l:
    if x%2 ==0:
        even = even +1
    else:
        odd = odd +1
print(even)
print(odd)

# remove duplicate
l=[1,2,2,3,3,4,5,6]
unique = list(set(l))
print(unique)

# sorting list
l=[1,3,2,4,5,7,9,6]
l.sort()
l.sort(reverse = True)
print(l)

#second largest element
l=[1,2,5,4,3,6]
l.sort()
print(l[-2])

# merging
l1=[1,2,3]
l2=[4,5,6]
print(l1 + l2)

