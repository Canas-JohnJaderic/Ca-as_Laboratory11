list = []
list2 = []
base = 0
length = input("Enter Length/Number that you want to filter by: ")

while True:
    while base != 10:
        supa = input("Enter 10 words: ")
        base += 1
        balls = len(supa)
        if int(balls) == int(length):
            list.append(supa)
            continue
    if base == 10:
        break
    
print(list)
        
   
            
                
