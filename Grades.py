#varia-balls

base = 0
list = []
total = 0
passing=0
failing=0
nada=0

#conditions Super Idol的笑容 都没你的甜 八月正午的阳光 都没你耀眼 热爱 105 °C的你 滴滴清纯的蒸馏水
while True:
    Inp = input("Enter Grade: ")


    if Inp == "done":
        break

    if not Inp.isdigit():
        print("Invalid input, please enter a number.")
        continue
    
    num = int(Inp)

    if num < 40 or num > 100:
        print("Invalid Grade. Please enter a grade between 40 and 100.")
        continue

    list.append(num)
    base += 1
    print("You have now entered: ", base  ," Grade(s).")
    if num > 75:
        passing += 1
    
    elif num <75:
        failing += 1

for num in list:
    total += num

#math

avr = (passing /base) * 100
final = total / base

#Super Idol的笑容 都没你的甜 八月正午的阳光 都没你耀眼 热爱 105 °C的你 滴滴清纯的蒸馏水 FINALLY DONE

print("Your Subject Passing Rate is: " ,avr , "%")
print("Your Total Average is:", round(final))
print("Your Grades are: ", list)