s = input().lower()

vowels = "aeiouy"
result = ""
for char in s: 
    if char not in vowels:
        result = result + "." + char
print (result) 
        