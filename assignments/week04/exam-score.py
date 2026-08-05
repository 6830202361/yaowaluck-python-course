# Assignment 2: If-else, loop + list
# โปรแกรมเพื่อการตรวจสอบผลการสอบ

scores = []

# รับคะแนนนักเรียน 5 คน
for i in range(5):
    score = int(input(f"Enter score of student {i+1}: "))
    scores.append(score)

print()

# ตรวจสอบผลสอบ
for i in range(5):
    if scores[i] >= 50:
        print(f"Student {i+1}: {scores[i]} -> ผ่าน")
    else:
        print(f"Student {i+1}: {scores[i]} -> ไม่ผ่าน")