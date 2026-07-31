"""
# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a, e, i. o u)
# โดยต้องใช้ loop-for ด้วยเท่านั้น

# ตัวอย่างหน้าจอ
# What is your name?: Yaowaluck
# Your text have 4 vowels.


name = input("What is your name?: ")
letters = list("Yaowaluck");/;/;/;llkSA
print(letter)

a = letter.count('a')
e = letter.count('e')
i = letter.count('i')
o = letter.count('o')
u = letter.count('u')

A = letter.count('A')
E = letter.count('E')
I = letter.count('I')
O = letter.count('O')
U = letter.count('U')

count = a + e + i + o + u + A + E + I + O + U
print("Your text have", count, "vowels")
"""

name = input("What is your name?: ")
count = 0 
for letter in name:
    if letter == 'a' or letter 'A':
            count = count +1
    elif letter == 'e' or letter 'E':
            count = count +1
    elif letter == 'i' or letter 'i':
            count = count +1
    elif letter == 'o' or letter 'O':
            count = count +1
    elif letter == 'u' or letter 'U':
            count = count +1

for letter in number:
    if letter in ["a", "e", "i", "o", "u", "A", "E", "i", "O","u"]:
        count = count + 1

#print(f"ตัวอักษร : {Letter}")
#print("Your text have", count, vowols")
"""