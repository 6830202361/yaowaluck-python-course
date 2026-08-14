# Example 3: Mathematical function
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
# Example 3: Mathematical function
def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 0.5 * {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

"""

เขียน Function แปลงหน่วยเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB

โดยใช้ชื่อและการใช้งาน
funtion convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองต้องเขียนด้วย

"""
def convert_currency(a, b)
    if b == "USD":\
        print(f"{a} THB = {a / 32.} USD")
    else:
        print(a, "USD =", {a * 32.} THB")

convert_currency(100, "USD")
convert_currency(100, "THB")