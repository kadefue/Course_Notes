x = input("How long should the series be?")
x = int(x)
while (x < 4):
    x = input("Sorry, the value should be greater than 3. How long should the series be?")
    x = int(x)
a1=1
a2=2
i =0
display = str(a1) + "," + str(a2)
while (i < x-2):
    a3 = a1 + a2 + 2
    display = display + "," + str (a3)
    a1=a2
    a2=a3
    i = i + 1
print(display)
