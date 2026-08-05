# Assignment 2: If-else, loop + list
# โปgnment 2รแกรมช่วยตัดสินใจเลือกซื้อสินค้าภายใต้งบประมาณรวม

prices = []
bought = []
total = 0

print("Enter prices of 6 items:")

# รับราคาสินค้า 6 รายการ
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)

print()

# รับงบประมาณรวม
budget = int(input("Enter total budget: "))
print()

# พิจารณาการซื้อสินค้า
for i in range(6):
    if total + prices[i] <= budget:
        print(f"Item {i+1} = {prices[i]} -> buy")
        total += prices[i]
        bought.append(prices[i])
    else:
        print(f"Item {i+1} = {prices[i]} -> cannot buy")

    print(f"Current total = {total}")
    print()

# แสดงผลลัพธ์
print("Bought items:", bought)
print("Total spent:", total)
print("Remaining budget:", budget - total)