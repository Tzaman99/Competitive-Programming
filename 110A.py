n = input()
num = 0

for i in n : 
    if i == '4' or i == '7':
        num += 1    
num = str(num)
for i in num:
    if i != '4' and i != '7':
        print("NO")
        break
else:
    print("YES")
                