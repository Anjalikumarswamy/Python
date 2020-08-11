# comment - Declare list and print.
# Using Visual studio code and to run on cmd - python <Filename>.py
nums = [1,2,3,4]
print(nums)

#appending 5 to the list.
nums.append(5)
print(nums)

#pop removes the last element by default
x = nums.pop()
y = nums.pop(1)
print(x)
print(y)
print(nums)


for x in nums:
    print(x)
print("Done")

#Tuples 
nums = 1,2,3,4
print(nums)

#Dictionary 
sal = {"jane":15, "John": 20}
print(sal)
#add andy to dict
sal["Andy"] = 24
print(sal)
#remove andy to dict
del sal["Andy"]
print(sal)

# it is key value pair 
for item in sal.keys():
    print(item)

for val in sal.items():
    print(item)

for keys, val in sal.items():
    print(item)

#python is case sensitive 
print("Jane" in sal)
print("jane" in sal)

#Sets 
s = {1,2,3}
print(type(s))
d={}
print(type(d))
s.add(1)
s.add(3)
s.add(4)
print(s)