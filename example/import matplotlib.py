print("========== คำนวณภาษีเงินได้ขั้นบันได ===========")

# รับค่าเงินได้สุทธิ
income = float(input("เงินได้สุทธิ (บาท): "))

tax = 0
remaining = income

# กำหนดช่วงภาษี
tax_brackets = [
    (150000, 0.00),
    (150000, 0.05),
    (200000, 0.10),
    (250000, 0.15),
    (250000, 0.20),
    (1000000, 0.25),
    (3000000, 0.30),
    (float("inf"), 0.35)
]

# ชื่อช่วงภาษี
labels = [
    "0 - 150,000",
    "150,001 - 300,000",
    "300,001 - 500,000",
    "500,001 - 750,000",
    "750,001 - 1,000,000",
    "1,000,001 - 2,000,000",
    "2,000,001 - 5,000,000",
    "มากกว่า 5,000,000"
]

tax_details = []

# คำนวณภาษีแต่ละขั้น
for i in range(len(tax_brackets)):
    limit, rate = tax_brackets[i]

    if remaining > 0:
        taxable = min(remaining, limit)
        tax_amount = taxable * rate
        tax += tax_amount
        tax_details.append((labels[i], tax_amount))
        remaining -= taxable
    else:
        tax_details.append((labels[i], 0))

# รายได้หลังหักภาษี
after_tax = income - tax

# Effective Tax Rate
if income > 0:
    effective_rate = (tax / income) * 100
else:
    effective_rate = 0

# แสดงผล
print("\n============== รายละเอียดภาษี ==============")

for label, amount in tax_details:
    print(f"{label:<25}{amount:>12,.2f} บาท")

print("-" * 42)
print(f"{'ภาษีรวม':<25}{tax:>12,.2f} บาท")
print(f"{'รายได้หลังหักภาษี':<25}{after_tax:>12,.2f} บาท")
print(f"Effective Tax Rate = {effective_rate:.2f}%")