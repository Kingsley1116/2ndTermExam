# 1-30偶數和

sum = 0

for i in range(1, 31):
    if i % 2 == 0:
        sum += i
print(f"1-30偶數和為 {sum}")