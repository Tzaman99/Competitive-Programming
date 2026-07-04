upper = input().strip()
lower = input().strip()

upper = upper.lower()
lower = lower.lower()

if upper<lower:
    print(-1)
elif upper>lower:
    print(1)
else:     
    print(0)    
        
