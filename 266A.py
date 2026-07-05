n = int(input())
s = input()

stone = 0
for i in range(n-1): 
    if s[i] == s[i+1]:
        stone += 1
print(stone)