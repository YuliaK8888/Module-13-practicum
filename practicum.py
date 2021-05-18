N = int(input("Put the numbers of tickets: "))
Total = 0
for i in range (N):
    age_L = int(input("Input age: "))
    if age_L < 18:
        price = 0
    elif 18 <= age_L < 25:
        price = 990
    elif age_L >= 25:
        price = 1390
    Total = Total + price

if N > 3:
    discount = Total*0.1
    fin_price = Total - discount
    print(fin_price)
else:
    print(Total)


