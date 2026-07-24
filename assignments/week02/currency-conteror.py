# Currency Converter

print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose option: ")

if choice == "1":
    thb = float(input("Enter amount (THB): "))
    usd = thb / 35.5
    print("Formula:", thb, "/ 35.5 =", format(usd, ".2f"))
    print("Result:", format(usd, ".2f"), "USD")

elif choice == "2":
    usd = float(input("Enter amount (USD): "))
    thb = usd * 35.5
    print("Formula:", usd, "* 35.5 =", format(thb, ".2f"))
    print("Result:", format(thb, ".2f"), "THB")

else:
    print("Invalid choice")