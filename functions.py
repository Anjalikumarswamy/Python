def downloadfile(url):
    print("Establish connection"+ url)
    print("Open connection")
    print("Close connection"+url)
    
downloadfile("ftp://www.google.com")

print("\n\n")

#function with return

def add(x,y): 
    return x + y

print(add(5,10))

print("\n\n")

#with Lamda function
add = lambda x, y : x + y

print(add(10,20))

#function within another function 

def multiply(x):
    return lambda y : x * y

multi = multiply(10)
print(multi(5))