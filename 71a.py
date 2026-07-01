n = int(input("Enter a number: "))
x=0
     for _ in range(n): 
         satement = input()
        if satement == "++X" or satement == "X++":
            x += 1
        else: 
            x -= 1
    print(x)           
            
    