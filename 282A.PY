n = int(input("Enter a number: "))
x = 0

for _ in range(n):
    statement = input()

    if statement == "++X" or statement == "X++":
        x += 1
    else:
        x -= 1

print(x)