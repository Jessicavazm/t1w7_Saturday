text = "Hello, World!"

# Extract Hello, it needs the colon 
print(text[:5])

# Extract World 
print(text[7:12])

# Extract everything, use [:]
print(text[:])

# Extract "World!" with step 2, leave the second holder empty, start = 7 stop = empty and step =2.
print(text[7::2])

# Reverse the string using [-1]
print(text[::-1])
