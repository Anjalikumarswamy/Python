#creating a text.txt file -'x' - create file
#f = open("text.txt",'x')
#f.close()

# with command 'w'- write to the file, 'a'-append to the file

with open("text.txt",'w') as f:
    f.write("Hello to Python")

with open("text.txt",'r') as f :
    for l in f.readline() : print(l)