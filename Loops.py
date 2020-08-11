# for Loops
for x in range(0,10):
    print(x)

print("done")

# break
nums = [y for y in range(0,10)]

for y in nums:
    if (y==4): break
    print(y)

print("done")

#continue
nums = [y for y in range(0,10)]

for y in nums:
    if (y==4): continue
    print(y)

print("done")

# While loop

a = 100
while a != 0:
    print (a)
    a -= 10

nums = [x for x in range(0,10)]
index = 0

while index < len(nums):
    print(nums[index])
    index +=1
print("done")